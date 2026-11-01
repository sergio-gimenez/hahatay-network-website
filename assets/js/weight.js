// What this visit downloaded, from the browser's Resource Timing (layouts/partials/extend-footer.html).
// transferSize is 0 for cached files and for cross-origin ones without Timing-Allow-Origin, so the
// figure is what actually crossed the network, never an estimate.
(function () {
  var out = document.getElementById("hh-weight");
  if (!out || !window.performance || !performance.getEntriesByType) return;

  function show() {
    var bytes = 0;
    ["navigation", "resource"].forEach(function (type) {
      performance.getEntriesByType(type).forEach(function (e) {
        bytes += e.transferSize || 0;
      });
    });
    out.textContent = out.dataset.template.replace("{kb}", Math.max(1, Math.round(bytes / 1024)));
    out.hidden = false;
  }

  window.addEventListener("load", function () {
    show();
    // Lazy images arrive after load; keep the figure current.
    if ("PerformanceObserver" in window) new PerformanceObserver(show).observe({ type: "resource" });
  });
})();
