# Forensics/Plane
**Writeup Author:** lolmenow

**Original Solver:** lolmenow

**Point Value:** 100pts

**Provided Files:**
  - plane.jpg

**Description:**
So many plane-related challenges! Why not another one? The flag is the latitude, longitude of the place this picture is taken from, rounded upto two decimal places. Example: n00bz{55.51,-20.27}. Author: NoobMaster Author: NoobMaster

# Solution

Use exiftool on the image. You will see GPS coordinates. That is the flag.

Final flag: `n00bz{13.37,-13.37}`
