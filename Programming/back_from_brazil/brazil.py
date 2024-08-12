import socket # used to connect to the server
import time # used to check for timeouts in data collection
addr = ("24.199.110.35", 43298) # address given for netcat
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s: # boilerplate socket stuff
    s.connect(addr) # connect to the address
    for i in range(10): # they made us get out of brazil 10 times
        data = b''
        start = time.time() # records time when data collection started
        while True: # this loop collects the data (the array given of eggs in brazil, plus some flavortext)
            if time.time()-start > 5:
                print('overtime!') # if data collection took more than 5 seconds something went wrong
                break
            chunk = s.recv(1048576) # 2^20
            if not chunk:
                break # if there is no more data, stop collecting
            data += chunk
            if len(set(chunk)) > 12:
                break
                # 12 accounts for digits, spaces, and line breaks
                # if len(set(chunk)) > 12 then chunk has text and has already been collected into data
                # it's very unlikely that we happen to lose a bit of text at the end
        message = data.decode()
        message = message.split('\n')
        del message[len(message)-1] # trims off text
        print(message[len(message)-1]) # debug print
        del message[len(message)-1] # trims off text
        arr = [msg.split(' ') for msg in message] # reconstructs 2D array given
        for i in range(len(arr)):
            del arr[i][1000] # there's an empty string leftover at the end of each line because there
            for j in range(len(arr[i])):
                arr[i][j] = int(arr[i][j]) # parse int from string
        print('arr constructed') # debug print
        best = [[0 for i in range(1000)] for j in range(1000)]
        # best is an array that keeps track of the most eggs you could collect going from (i,j) to (999,999)
        path = [['' for i in range(1000)] for j in range(1000)]
        # path is the path (in string form) that will collect the amount of eggs given in best
        best[999][999] = arr[999][999] # the best you can do when you're already at the end is the eggs there
        path[999][999] = '' # this is technically redundant but makes it clear that path[999][999] will be ''

        for i in range(999):
            best[999][999-i-1] = best[999][999-i]+arr[999][999-i-1]
            best[999-i-1][999] = best[999-i][999]+arr[999-i-1][999]
        print('first DPing done') # debug print
        for i in range(999):
            for j in range(999):
                best[998-i][998-j] = max(best[998-i][998-j+1],best[998-i+1][998-j])+arr[998-i][998-j]
        print('second DPing done') # debug print
        print('best: '+str(best[0][0]))
        for i in range(999):
            path[999][999-i-1] = 'd'+path[999][999-i]
            path[999-i-1][999] = 'r'+path[999-i][999]
        print('third DPing done') # debug print
        for i in range(999):
            for j in range(999):
                if best[998-i][998-j] == best[998-i][998-j+1]+arr[998-i][998-j]:
                    path[998-i][998-j] = 'd'+path[998-i][998-j+1]
                elif best[998-i][998-j] == best[998-i+1][998-j]+arr[998-i][998-j]:
                    path[998-i][998-j] = 'r'+path[998-i+1][998-j]
                else:
                    print('ERROR IN BEST; NOOOO!!!') # if there was an error in best, it would be really bad since I thought it worked
        print('final DPing done and sending:')

        print(path[0][0]) # print what is sent for debugging
        s.send((path[0][0]+'\n').encode()) # sends answer
    flag = s.recv(1024).decode() # after ten escapes from brazil, the flag is sent
    print(flag) # program prints flag for user