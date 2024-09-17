import sys
sys.setrecursionlimit(10 ** 5)

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