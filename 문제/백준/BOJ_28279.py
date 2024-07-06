from collections import deque
import sys

N = int(sys.stdin.readline())

deque = deque()

for i in range(N):
    arr = list(map(int,sys.stdin.readline().split()))
    if(arr[0] == 1):
        deque.appendleft(arr[1])
    elif(arr[0] == 2):
        deque.append(arr[1])
    elif(arr[0] == 3):
        if(deque):
            a = deque.popleft()
            print(a)
        else:
            print(-1)
    elif(arr[0] == 4):
        if(deque):
            a = deque.pop()
            print(a)
        else:
            print(-1)
    elif(arr[0] == 5):
        print(len(deque))
    elif(arr[0] == 6):
        if(deque):
            print(0)
        else:
            print(1)
    elif(arr[0] == 7):
        if(deque):
            print(deque[0])
        else:
            print(-1)
    elif(arr[0] == 8):
        if(deque):
            print(deque[-1])
        else:
            print(-1)