from pwn import *

p = process(['python3', 'server.py'])

a = list(map(int, p.recvline().decode().split()))

for i in range(17):
    val = (min(a) + max(a)) // 2
    val -= val % 2
    
    a = [abs(val - x) for x in a]
    print(len(set(a)))
    if len(set(a)) < 10: print(set(a)) 
    
    p.sendline(str(val).encode())

p.sendline(str(3).encode())
a = [abs(3 - x) for x in a]
print(len(set(a)))
if len(set(a)) < 10: print(set(a)) 

p.sendline(str(1).encode())
a = [abs(1 - x) for x in a]
print(len(set(a)))
if len(set(a)) < 10: print(set(a)) 

p.sendline(str(1).encode())
a= [abs(1 - x) for x in a]
print(len(set(a)))
if len(set(a)) < 10: print(set(a)) 

p.interactive()