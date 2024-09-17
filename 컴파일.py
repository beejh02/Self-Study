<<<<<<< HEAD
import sys

N, M = map(int,sys.stdin.readline().split())

arr = [[0 for i in range(N)] for i in range(N)]
visited = [0 for i in range(N)]
cnt = 0

for i in range(M):
    x, y = map(int,sys.stdin.readline().split())
    arr[x-1][y-1] = 1
    arr[y-1][x-1] = 1

def DFS(V):
    visited[V] = 1
    for i in range(N):
        if(arr[V][i] == 1 and visited[i] == 0):
            DFS(i)

while not all(visited):
    for i in range(len(visited)):
        if(visited[i] == 0):
            cnt += 1
            DFS(i)

sys.stdout.write(str(cnt))
=======
from collections import deque

N, M = map(int,input().split())

queue = deque([N])
arr = [0 for i in range(200001)]
arr[N] = 1
cnt = 0

while(queue):
    for i in range(len(queue)):
        x = queue.popleft()
        if(x == M):
            print(cnt)
            exit()
        for nx in (x-1, x+1, x*2):
            if(0 < nx <= 200000 and arr[nx] == 0):
                arr[nx] = 1
                queue.append(nx)
    cnt += 1

print(cnt)
>>>>>>> ed7edf007a7334a19673b6e4d587b073f48260c7
