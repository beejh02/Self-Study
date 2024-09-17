import sys
from collections import deque

N, M = map(int,sys.stdin.readline().split())

queue = deque([N])
arr = [0 for i in range(100001)]
arr[N] = 1
cnt = 0

while(queue):
    for i in range(len(queue)):
        x = queue.popleft()
        if(x == M):
            sys.stdout.write(str(cnt))
            exit()
        for nx in (x-1, x+1, x*2):
            if(0 <= nx <= 100000 and arr[nx] == 0):
                arr[nx] = 1
                queue.append(nx)
    cnt += 1