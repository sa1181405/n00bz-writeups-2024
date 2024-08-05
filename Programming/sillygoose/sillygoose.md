# Sillygoose
Writeup author: **wjat**
Point count: 267

Provided files: [sillygoose.py](https://static.n00bzunit3d.xyz/Programming/Sillygoose/sillygoose.py)

Description: There's no way you can guess my favorite number, you silly goose. Author: Connor Chang

# Solution
This is a simple binary search challenge. Two possible responses are "your answer is too large you silly goose" and "your answer is too small you silly goose". Taking the 19th (0-indexed) character allows differentiation between these two.
```python
import socket
addr = ("24.199.110.35", 41199)
g1 = 0
g2 = 10**100
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect(addr)
    s.send((str((g1+g2)//2)+'\n').encode())
    while True:
        data = s.recv(100)
        if not data:
            break
        message = data.decode()
        print(message)
        if message[19] == 's':
            g1 = (g1+g2)//2
        else:
            g2 = (g1+g2)//2
        s.send((str((g1+g2)//2)+'\n').encode())
```
Note that the program loops indefinitely and must be stopped after obtaining the flag.

Final flag: `n00bz{y0u_4r3_4_sm4rt_51l1y_g0053}`