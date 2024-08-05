# Numbers 2
Writeup author: **wjat**

# Solution

Here is the code used to solve this challenge, with comments to explain some things.
```py
import math
import socket

#gpd = greatest prime divisor
def gpd(n):
    largest_prime = -1
    i = 2
    while i * i <= n:
        while n % i == 0:
            largest_prime = i
            n = n // i
        i = i + 1
    if n > 1:
        largest_prime = n
    return largest_prime

addr = ("challs.n00bzunit3d.xyz", 10529)
i = 0
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect(addr)
    while True:
        data = s.recv(300)
        if not data:
            break
        message = data.decode()
        print(message)
        # order of ifs: lcm, gcd, gpd
        message = message.split('\n')
        message = message[len(message)-1] # takes the last line of the message, which will have the number(s)
        if message[21] == 'm': 
            message = message[37:-2].split(' and ') # creates a list with the two numbers
            answer = 1
            try:
                answer = math.lcm(int(message[0]),int(message[1]))
            except:
                print('Error or end')
        elif message[21] == 'c': 
            message = message[39:-2].split(' and ') # creates a list with the two numbers
            answer = 1
            try:
                answer = math.gcd(int(message[0]),int(message[1]))
            except:
                print('Error or end')
        else:
            message = message[37:-2] # crops the message to the number
            answer = 1
            try:
                answer = gpd(int(message))
            except:
                print('Error or end')
        s.send((str(answer)+'\n').encode()) # sending answer (with a line break so it's inputted)
```