from collections import deque
import sys

n = int(sys.stdin.readline())

queue = deque()

for i in range(n):
    arr = list(map(str,sys.stdin.readline().split()))
    
    if(arr[0] == "push"):
        queue.append(arr[1])
    elif(arr[0] == "pop"):
        try:
            print(queue.popleft())
        except:
            print(-1)
    elif(arr[0] == "size"):
        print(len(queue))
    elif(arr[0] == "empty"):
        if(len(queue) == 0):
            print(1)
        else:
            print(0)
    elif(arr[0] == "front"):
        try:
            print(queue[0])
        except:
            print(-1)
    elif(arr[0] == "back"):
        try:
            print(queue[-1])
        except:
            print(-1)