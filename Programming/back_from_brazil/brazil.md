# Solution

Examining the source code for the chall, we find that a large integer array is printed with egg amounts. Our goal is to find a path only involving right ('r') and down ('d') moves that maximizes eggs. We must do this 10 times.

### Start
```py
import socket
import time
addr = ("24.199.110.35", 43298)
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect(addr)
    for i in range(10):
```
This is just some boilerplate stuff to connect to the server. The rest of the code will be in a loop that runs 10 times (except for the last couple of lines).
### Data Collection
```py
        data = b''
        start = time.time()
        while True:
            if time.time()-start > 5:
                print('overtime!')
                break
            chunk = s.recv(1048576) # 2^20
            if not chunk:
                break
            data += chunk
            if len(set(chunk)) > 12:
                break
```
Here, we record the time when data collection starts in `start`. Then, we run a forever loop that recieves 2^20 bytes each time, and is broken when data is finished collecting. The source code for the chall tells us that the data is an integer array in the form of digits, spaces, line breaks, and some flavortext at the end, including the maximal number of eggs. There are several signs that we use to detect the end of data collection.
- It's taking more than 5 seconds. (This is a fail-safe.)
- The latest collection didn't collect anything.
- The latest collection contains more characters than digits and whitespace.
Technically, there is a tiny chance that the third condition will end the loop 1 chunk early because text is split between two chunks, but in practice the large size of the chunks will mostly prevent this.
### Data Parsing
```py
        message = data.decode()
        message = message.split('\n')
        del message[len(message)-1]
        print(message[len(message)-1])
        del message[len(message)-1]
        arr = [msg.split(' ') for msg in message]
        for i in range(len(arr)):
            del arr[i][1000]
            for j in range(len(arr[i])):
                arr[i][j] = int(arr[i][j])
        print('arr constructed')
```
Now that we have our `data`, we decode it from bytes to a string `message`, then split `message` into lines. There are a couple of deletions to trim off the flavortext, and one of the text lines is printed (the maximal number of eggs) for debugging. Then, `message` is further split by spaces into `arr`. Due to the formatting of the data, we end up with an extra empty string at the end of each row of `arr`, which must be deleted. Finally, the rest of `arr` is parsed from strings to integers, and a debug message is printed.
### Pre-Solving
```py
        best = [[0 for i in range(1000)] for j in range(1000)]
        # 
        path = [['' for i in range(1000)] for j in range(1000)]
        # path is the path (in string form) that will collect the amount of eggs given in best
        best[999][999] = arr[999][999]
        path[999][999] = ''
```
Two arrays are created to be used during solving:
- `best[i][j]` keeps track of the most eggs you could collect going from (i,j) to (999,999)
- `path[i][j]` gives the path (in 'r' and 'd') to follow to obtain `best[i][j]` eggs
The starting values (for [999][999]) are also set.
### Solving Pt.1
```py
        for i in range(998,-1,-1):
            best[999][i] = best[999][i+1]+arr[999][i]
            best[i][999] = best[i+1][999]+arr[i][999]
        print('first DPing done')
        for i in range(998,-1,-1):
            for j in range(998,-1,-1):
                best[i][j] = max(best[i][j+1],best[i+1][j])+arr[i][j]
        print('second DPing done')
        print('best: '+str(best[0][0]))
```
From (999,?) and (?,999), there's only one direction to go to get to (999,999). So, it's pretty easy to calculate the `best` recursively on the bottom row and rightmost column. Then, a debug message is printed.

Then, for each point (i,j) with i,j < 999, the `best` from (i,j) is the number of eggs at (i,j) plus the maximum of the `best` from (i+1,j) and the `best` from (i,j+1). This is put into script to solve for `best` recursively. Finally, `best[0][0]`, the overall best, is printed to check again the number given by the server for debugging.
### Solving Pt.2
```py
        for i in range(998,-1,-1):
            path[999][i] = 'd'+path[999][i+1]
            path[i][999] = 'r'+path[i+1][999]
        print('third DPing done')
        for i in range(998,-1,-1):
            for j in range(998,-1,-1):
                if best[i][j] == best[i][j+1]+arr[i][j]:
                    path[i][j] = 'd'+path[i][j+1]
                elif best[i][j] == best[i+1][j]+arr[i][j]:
                    path[i][j] = 'r'+path[i+1][j]
                else:
                    print('ERROR IN BEST; NOOOO!!!')
```
The first three lines of pt.2 are similar to the first three lines of pt.1. From (999,?) and (?,999), there's only one direction to go to get to (999,999). So, it's pretty easy to construct the `path` recursively on the bottom row and rightmost column. Then, a debug message is printed.

At this point, best has already been fully calculated, so we can refer to it during our construction of `path`. If `best[i][j] == best[i][j+1]+arr[i][j]` then `path[i][j]` must pass through (i,j+1) and start with 'd'. If `best[i][j] == best[i+1][j]+arr[i][j]` then `path[i][j]` must pass through (i+1,j) and start with 'r'. If best was constructed correctly, one of these must be the case, so a debug message is printed neither checks out. This is put into script to solve for `path` recursively.
### Final Lines
```py
        print('final DPing done and sending:')
        print(path[0][0])
        s.send((path[0][0]+'\n').encode())
    flag = s.recv(1024).decode()
    print(flag)
```
Finally, `path[0][0]`, the overall optimal `path` being sent, is printed for debugging, and the 10-loop starts anew. After 10 iterations, the challenge is complete, and the message from the server containing the flag is printed.

Final flag:
`n00bz{y0u_g0t_m3_b4ck_h0m3!}`
