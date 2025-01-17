---
title: "Mount external HDD Permanently to any Linux  Machine"
date: 2023-04-22
---

List all disks and partitions with:

```bash
sudo fdisk -l
```

Listed the UUID of the hard drive or logical partition you would like to mount permanently:

```bash
sudo blkid /dev/sdb
```

It should show something like:

```source
/dev/sdb: UUID="ac34863b-062d-4a37-a1c6-e4c4313fbfa2" BLOCK_SIZE="4096" TYPE="ext4"
```

Create the target location (the directory) where the nextcloud volumes will be stored, in my case

```bash
mkdir nextcloud_data
```

Now mount the drive in the created directory:

```bash
sudo mount /dev/sdb ./nextcloud_data/
```

Now, in order to make the mount we just did to persist after reboots, we need to put the mounted partition in the `/etc/fstab` file.

Let's first make a backup just in case:

```bash
sudo cp /etc/fstab /etc/fstab.bkp
```

To avoid breaking the file system you need to look at the structure that is already in `/etc/fstab` for the disks that are already automounted. In my case it is like this:

```bash
hahatay@nuc2:~/self-hosted-docker-server/office-server/nextcloud$ sudo cat /etc/fstab
# /etc/fstab: static file system information.
#
# Use 'blkid' to print the universally unique identifier for a
# device; this may be used with UUID= as a more robust way to name devices
# that works even if disks are added and removed. See fstab(5).
#
# <file system> <mount point>   <type>  <options>       <dump>  <pass>
# / was on /dev/ubuntu-vg/ubuntu-lv during curtin installation
/dev/disk/by-id/dm-uuid-LVM-2UVIzfTi2Y4LKFIkALpDC4pzDAdHOZcNBq0U4M1SIVlWWv2oWb4B8QmLfSKG1dgH / ext4 defaults 0 1
# /boot was on /dev/sda2 during curtin installation
/dev/disk/by-uuid/d533c7f4-99fd-42fa-a2ce-391a788fa59c /boot ext4 defaults 0 1
# /boot/efi was on /dev/sda1 during curtin installation
/dev/disk/by-uuid/111E-88A3 /boot/efi vfat defaults 0 1
/swap.img	none	swap	sw	0	0
```

More info about what this fields mean can be found in the [ArchLinux Wiki](https://wiki.archlinux.org/title/Fstab).

Now, let's edit the `/etc/fstab` file with your favourite editor:

```bash
sudo vim /etc/fstab
```

In my case, I added the following line: 

```source
/dev/disk/by-uuid/ac34863b-062d-4a37-a1c6-e4c4313fbfa2 /home/hahatay/self-hosted-docker-server/office-server/nextcloud/nextcloud_data ext4 defaults 0 2
```

Now it can be tested by restarting the machine and see that the mount is still there.