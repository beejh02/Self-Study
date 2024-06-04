"""

4 5 1
1 2
1 3
1 4
2 4
3 4


"""
from collections import deque
import sys

N, M, V = map(int,sys.stdin.readline().split())

arr = [[0 for i in range(N+1)]for i in range(N+1)]

for i in range(M):
    x,y = map(int,sys.stdin.readline().split())
    arr[x][y] = 1
    arr[x][y] = 1

visited_D = [0]*(N+1)
visited_B = [0]*(N+1)


def DFS(V):
    visited_D[V] = 1
    sys.stdout.write(str(V) + " ")
    for i in range(1, N+1):
        if(arr[V][i] == 1 and visited_D[i] == 0):
            DFS(i)

def BFS(V):
    queue = deque([V])
    sys.stdout.write(str(V) + " ")
    while(queue):
        V = queue.popleft()
        for i in range(1, N+1):
            if(arr[V][i] == 1 and visited_B[i] == 0):
                visited_B[i] = 1
                queue.appendleft(i)
                sys.stdout.write(str(i) + " ")

DFS(V)
print()
BFS(V)
