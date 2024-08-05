# programming/sillygoose
**Writeup Author:** lolmenow

**Original Solver:** lolmenow

**Point Value:** 2__

**Provided Files:**
  - sillygoose.py
  - nc 24.199.110.35 41199

**Description:**
There's no way you can guess my favorite number, you silly goose. Author: Connor Chang

# Solution

Reading the python code, you can see this is obviously a classic case of binary search.

Here is the (obviously chatgpt written) script that can solve this:

```
import socket
import time

# Connect to the server
host = '24.199.110.35'
port = 41199
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))

# Binary search setup
low = 0
high = 10**100
turns = 0
start_time = time.time()

while True:
    turns += 1
    mid = (low + high) // 2
    s.sendall(f"{mid}\n".encode())
    response = s.recv(1024).decode().strip()

    if "too large" in response:
        high = mid - 1
    elif "too small" in response:
        low = mid + 1
    elif "congratulations" in response:
        print(response)
        flag = s.recv(1024).decode().strip()
        print(flag)
        break
    elif "ran out of time" in response or "no fun" in response or "skill issue" in response:
        print(response)
        break

    if time.time() > start_time + 60:
        print("Ran out of time")
        break

s.close()
```

Final flag: `n00bz{y0u_4r3_4_sm4rt_51l1y_g0053}`
