#!/usr/bin/env python3
"""Draws the home-page map of Gandiol, and its Saint-Louis inset, from OpenStreetMap.

    python3 tools/map.py            # fetch from Overpass (cached in tools/.osm-cache/), write the maps
    python3 tools/map.py --refresh  # ignore the cache

Writes layouts/partials/home/map-osm-<frame>.html (the geography as SVG paths, for map.html to
inline) and data/mapframe.yaml (each frame and its size, which map.html uses to place the nodes
from their lat/lon). All are committed, so building the site never needs the network. Map data
© OpenStreetMap contributors, ODbL: the credit is shown under the map.
"""
import hashlib
import json
import math
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CACHE = ROOT / "tools" / ".osm-cache"
OVERPASS = "https://overpass-api.de/api/interpreter"

PAD = 20  # geometry is kept this far outside a frame, so strokes don't end at the edge


class Frame:
    """An area to draw (south, west, north, east), its width in SVG units, whether to show buildings,
    and the grid that coordinates are rounded to (coarser is lighter)."""

    def __init__(self, name, s, w, n, e, width, buildings, grid):
        self.name, self.s, self.w, self.n, self.e = name, s, w, n, e
        self.width, self.buildings, self.grid = width, buildings, grid
        self.kx = math.cos(math.radians((s + n) / 2))
        self.scale = width / ((e - w) * self.kx)  # SVG units per degree of latitude
        self.height = round((n - s) * self.scale, 1)

    def project(self, p):
        return ((p["lon"] - self.w) * self.kx * self.scale, (self.n - p["lat"]) * self.scale)


FRAMES = [
    # Tassinère and Ndiébène, the Langue de Barbarie and a strip of ocean.
    Frame("gandiol", 15.870, -16.523, 15.901, -16.493, 400, buildings=True, grid=0.1),
    # The island of Saint-Louis with Sor and Guet Ndar, drawn as an inset: Jangkom is at its north tip.
    # Its dense street grid is what makes it recognisable, so streets stay in, on a coarser grid.
    Frame("saint_louis", 16.010, -16.514, 16.046, -16.484, 112, buildings=False, grid=0.5),
]


def overpass(name, query):
    CACHE.mkdir(exist_ok=True)
    # Keyed by the query too, so moving a frame fetches its new area instead of reusing the old one.
    cached = CACHE / f"{name}-{hashlib.sha1(query.encode()).hexdigest()[:8]}.json"
    if cached.exists() and "--refresh" not in sys.argv:
        return json.loads(cached.read_text())
    req = urllib.request.Request(OVERPASS, data=urllib.parse.urlencode({"data": query}).encode(),
                                 headers={"User-Agent": "hahatay-network-website/map.py"})
    for wait in (30, 60, 120, None):  # the public server often answers "busy": back off and retry
        try:
            with urllib.request.urlopen(req, timeout=300) as r:
                body = r.read()
            break
        except urllib.error.HTTPError as err:
            if wait is None or err.code not in (429, 502, 503, 504):
                raise
            print(f"Overpass busy ({err.code}), retrying in {wait} s")
            time.sleep(wait)
    cached.write_bytes(body)
    return json.loads(body)


# ── geometry helpers ─────────────────────────────────────────────────────────

def join(ways):
    """Joins ways that share end nodes into chains (closed rings for polygons)."""
    ways = [list(w) for w in ways if len(w) > 1]
    chains = []
    while ways:
        chain = ways.pop()
        grown = True
        while grown and chain[0] != chain[-1]:
            grown = False
            for i, w in enumerate(ways):
                if w[0] == chain[-1]:
                    chain += w[1:]
                elif w[-1] == chain[-1]:
                    chain += w[-2::-1]
                elif w[-1] == chain[0]:
                    chain = w[:-1] + chain
                elif w[0] == chain[0]:
                    chain = w[:0:-1] + chain
                else:
                    continue
                ways.pop(i)
                grown = True
                break
        chains.append(chain)
    return chains


def clip(ring, x1, y1, x0=-PAD, y0=-PAD):
    """Sutherland–Hodgman: a polygon ring cut to the rectangle."""
    def cut(pts, inside, cross):
        out = []
        for i, cur in enumerate(pts):
            prev = pts[i - 1]
            if inside(cur):
                if not inside(prev):
                    out.append(cross(prev, cur))
                out.append(cur)
            elif inside(prev):
                out.append(cross(prev, cur))
        return out

    def at_x(x):
        return lambda a, b: (x, a[1] + (b[1] - a[1]) * (x - a[0]) / (b[0] - a[0]))

    def at_y(y):
        return lambda a, b: (a[0] + (b[0] - a[0]) * (y - a[1]) / (b[1] - a[1]), y)

    pts = ring
    for inside, cross in ((lambda p: p[0] >= x0, at_x(x0)), (lambda p: p[0] <= x1, at_x(x1)),
                          (lambda p: p[1] >= y0, at_y(y0)), (lambda p: p[1] <= y1, at_y(y1))):
        if not pts:
            break
        pts = cut(pts, inside, cross)
    return pts


def simplify(pts, tol):
    """Ramer–Douglas–Peucker."""
    if len(pts) < 3:
        return pts
    keep = [False] * len(pts)
    keep[0] = keep[-1] = True
    stack = [(0, len(pts) - 1)]
    while stack:
        a, b = stack.pop()
        (ax, ay), (bx, by) = pts[a], pts[b]
        dx, dy = bx - ax, by - ay
        norm = math.hypot(dx, dy) or 1e-9
        far, idx = 0, None
        for i in range(a + 1, b):
            d = abs(dy * (pts[i][0] - ax) - dx * (pts[i][1] - ay)) / norm
            if d > far:
                far, idx = d, i
        if idx is not None and far > tol:
            keep[idx] = True
            stack += [(a, idx), (idx, b)]
    return [p for p, k in zip(pts, keep) if k]


def near(pts, f):
    xs, ys = [p[0] for p in pts], [p[1] for p in pts]
    return max(xs) >= -PAD and min(xs) <= f.width + PAD and max(ys) >= -PAD and min(ys) <= f.height + PAD


def num(v):
    """Shortest form on a 0.1 grid: 12, .5, -.5."""
    s = f"{v:.1f}".rstrip("0").rstrip(".")
    if s.startswith("-0."):
        s = "-" + s[2:]
    elif s.startswith("0."):
        s = s[1:]
    return "0" if s in ("-0", "-") else s


def path(lines, grid, closed=False):
    """Polylines as compact path data: absolute start, then relative steps on the grid."""
    out = []
    for pts in lines:
        q = [(round(x / grid) * grid, round(y / grid) * grid) for x, y in pts]
        q = [p for i, p in enumerate(q) if i == 0 or p != q[i - 1]]
        if len(q) < 2:
            continue
        d = f"M{num(q[0][0])} {num(q[0][1])}l" + " ".join(
            f"{num(b[0] - a[0])} {num(b[1] - a[1])}" for a, b in zip(q, q[1:]))
        out.append(d.replace(" -", "-") + ("z" if closed else ""))
    return "".join(out)


def dots(points):
    """Many dots in one path: each is a zero-length segment drawn with a round cap."""
    q = sorted({(round(x, 1), round(y, 1)) for x, y in points}, key=lambda p: (round(p[1] / 6), p[0]))
    if not q:
        return ""
    out, (px, py) = [f"M{num(q[0][0])} {num(q[0][1])}h0"], q[0]
    for x, y in q[1:]:
        out.append(f"m{num(x - px)} {num(y - py)}h0".replace(" -", "-"))
        px, py = x, y
    return "".join(out)


# ── data ─────────────────────────────────────────────────────────────────────

def draw(f):
    box = f"{f.s - 0.004},{f.w - 0.004},{f.n + 0.004},{f.e + 0.004}"
    # Areas with their full geometry, so multipolygon rings come back closed.
    areas = overpass(f"{f.name}-areas", f"""[out:json][timeout:200];
        (way["natural"="coastline"]({box});
         way["natural"~"^(water|beach|sand|wood|scrub|wetland)$"]({box}); way["landuse"="forest"]({box});
         relation["natural"~"^(water|beach|sand|wood|scrub|wetland)$"]({box}););
        out geom;""")
    # Streets (and buildings, where the frame shows them), cut to the box.
    lines = overpass(f"{f.name}-lines", f"""[out:json][timeout:200];
        (way["highway"]({box});{f' way["building"]({box});' if f.buildings else ""});
        out geom({box});""")

    water, sand, green, coast = [], [], [], []
    layer = {"water": water, "beach": sand, "sand": sand}  # anything else is vegetation
    for e in areas["elements"]:
        t = e.get("tags", {})
        kind = t.get("natural")
        if e["type"] == "way":
            pts = [f.project(p) for p in e["geometry"]]
            if kind == "coastline":
                coast.append(pts)
            elif pts[0] == pts[-1]:
                layer.get(kind, green).append(pts)
        else:
            members = [[f.project(p) for p in m["geometry"]] for m in e["members"] if m.get("geometry")]
            layer.get(kind, green).extend(join(members))

    # The ocean: the coastline north to south, closed far out to the west.
    ocean = []
    for chain in join(coast):
        if not near(chain, f):
            continue
        if chain[0][1] > chain[-1][1]:
            chain = chain[::-1]
        ocean.append(chain + [(-10 * f.width, chain[-1][1]), (-10 * f.width, chain[0][1])])

    def polys(rings, tol):
        # A ring is simplified as two halves, split at its farthest point from the start: with
        # both ends on the same point, Douglas–Peucker would have no baseline to measure from.
        out = []
        for r in rings:
            r = clip(r, f.width + PAD, f.height + PAD)
            if len(r) < 3:
                continue
            far = max(range(len(r)), key=lambda i: math.dist(r[0], r[i]))
            ring = simplify(r[:far + 1], tol) + simplify(r[far:] + [r[0]], tol)[1:-1]
            if len(ring) > 2:
                out.append(ring)
        return out

    main_roads, minor_roads, homes = [], [], []
    for e in lines["elements"]:
        t = e.get("tags", {})
        pts = [f.project(p) for p in e.get("geometry", []) if p]
        if len(pts) < 2 or not near(pts, f):
            continue
        if "building" in t:
            homes.append((sum(p[0] for p in pts) / len(pts), sum(p[1] for p in pts) / len(pts)))
        elif t["highway"] in ("trunk", "primary", "secondary", "tertiary", "unclassified"):
            main_roads.append(pts)
        elif t["highway"] in ("residential", "service", "track", "living_street"):
            minor_roads.append(pts)
    # Streets that meet end to end become one line: fewer moves in the path data.
    main_roads = [simplify(r, 0.4) for r in join(main_roads)]
    minor_roads = [simplify(r, 0.5) for r in join(minor_roads)]

    out = ROOT / "layouts" / "partials" / "home" / f"map-osm-{f.name.replace('_', '-')}.html"
    out.write_text(
        f"{{{{/* Generated by tools/map.py on {date.today()} from OpenStreetMap "
        f"(© OpenStreetMap contributors, ODbL). Don't edit: run the script. */}}}}\n"
        f'<path class="hh-ocean" d="{path(polys(ocean, 0.4), f.grid, True)}" />\n'
        f'<path class="hh-sand" fill-rule="evenodd" d="{path(polys(sand, 0.5), f.grid, True)}" />\n'
        f'<path class="hh-green" fill-rule="evenodd" d="{path(polys(green, 0.5), f.grid, True)}" />\n'
        f'<path class="hh-water" fill-rule="evenodd" d="{path(polys(water, 0.4), f.grid, True)}" />\n'
        f'<path class="hh-road" d="{path(minor_roads, f.grid)}" />\n'
        f'<path class="hh-road-main" d="{path(main_roads, f.grid)}" />\n'
        + (f'<path class="hh-homes" d="{dots(homes)}" />\n' if homes else ""))
    print(f"{out.relative_to(ROOT)}: {out.stat().st_size // 1024} KB · {len(homes)} buildings, "
          f"{len(main_roads) + len(minor_roads)} streets, {len(water)} water rings, {len(ocean)} coast")


def main():
    for f in FRAMES:
        draw(f)
    (ROOT / "data" / "mapframe.yaml").write_text(
        "# Written by tools/map.py: each map's frame (degrees) and its size in SVG units.\n" + "".join(
            f"{f.name}:\n  south: {f.s}\n  west: {f.w}\n  north: {f.n}\n  east: {f.e}\n"
            f"  width: {f.width}\n  height: {f.height}\n" for f in FRAMES))


if __name__ == "__main__":
    main()
