from collections import deque
import sys

N, M, V = map(int,sys.stdin.readline().split())

arr = [[0]*(N+1) for _ in range(N+1)]
visited_D = [0]*(N+1)
visited_B = [0]*(N+1)

for i in range(M):
    a,b = map(int,sys.stdin.readline().split())
    arr[a][b] = 1
    arr[b][a] = 1

def DFS(V):
    visited_D[V] = 1
    sys.stdout.write(str(V) + " ")
    for i in range(1,N+1):
        if(arr[V][i] == 1 and visited_D[i] == 0):
            DFS(i)

def BFS(V):
    queue = deque([V])
    visited_B[V] = 1
    sys.stdout.write(str(V) + " ")
    while queue:
        V = queue.popleft()
        for i in range(1, N+1):
            if(arr[V][i] == 1 and not visited_B[i]):
                visited_B[i] = 1
                queue.append(i)
                sys.stdout.write(str(i) + " ")

DFS(V)
print()
BFS(V)