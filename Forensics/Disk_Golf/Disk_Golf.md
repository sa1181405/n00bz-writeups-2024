# 🩸Forensics/Disk Golf
**Writeup Author:** lolmenow

**Original Solver:** lolmenow

**Point Value:** 4__

**Provided Files:**
  - [disk.img.tar.gz](https://static.n00bzunit3d.xyz/Forensics/Disk-Golf/disk.img.tar.gz)

**Description:**
Let's play some disk golf! Author: NoobMaster

# Solution

Download the disk image, use [autopsy](https://www.autopsy.com/) on the disk file (set the disk type to volume).

Use the file search, and search for "flag.txt"

We find a file containing a sequence of numbers: `156 60 60 142 172 173 67 150 63 137 154 60 156 147 137 64 167 64 61 164 63 144 137 144 61 65 153 137 146 60 162 63 156 163 61 143 65 175`

This is octal, decrypt using cyberchef.

[Recipe](https://gchq.github.io/CyberChef/#recipe=From_Octal('Space')&input=MTU2IDYwIDYwIDE0MiAxNzIgMTczIDY3IDE1MCA2MyAxMzcgMTU0IDYwIDE1NiAxNDcgMTM3IDY0IDE2NyA2NCA2MSAxNjQgNjMgMTQ0IDEzNyAxNDQgNjEgNjUgMTUzIDEzNyAxNDYgNjAgMTYyIDYzIDE1NiAxNjMgNjEgMTQzIDY1IDE3NQ)

Final flag: `n00bz{7h3_l0ng_4w41t3d_d15k_f0r3ns1c5}`
