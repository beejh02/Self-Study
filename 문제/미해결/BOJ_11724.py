from collections import deque

queue = deque()
N, M = map(int,input().split())

arr = [[0 for i in range(N)] for i in range(N)]
visited = [0 for i in range(N)]

for i in range(M):
    u, v = map(int,input().split())
    arr[u-1][v-1] = 1
    arr[v-1][u-1] = 1

for i in range(N):
    for j in range(N):
        if(arr[i][j] == 1):
            if(visited[i][j] == 0):
                queue.append((i,j))
                visited[j] = 1
            else:
                

