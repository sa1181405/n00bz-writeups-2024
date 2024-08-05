# 🩸 Rev/vacation
**Writeup Author:** lolmenow
**Original Solver:** lolmenow
**Point Value:** 100

**Provided Files:**
  - run.ps1
  - output.txt

**Description:**
My friend told me they were going on vacation, but they sent me this weird PowerShell script instead of a postcard! Author: 0xBlue

# Solution

The powershell script is simplying xoring the output with the key of `3`

Just xor the output with the key of `3`

[Recipe](https://gchq.github.io/CyberChef/#recipe=XOR(%7B'option':'Hex','string':'3'%7D,'Standard',false)&input=bTMzYXl4ZXFsblxzYnFqcFx0d2tce2xxfgo)

Final flag: `n00bz{from_paris_wth_xor}`
