import sys
from collections import deque

N, M = map(int,input().split())

arr = []
queue = deque()

directinos = [(-1,0), (0,1), (1,0), (0,-1)]


###
# 입력한 배열 넣어주기
for i in range(M):
  arr.append(list(map(int,input().split())))

###

for i in range(M):
  for j in range(N):
    if(arr[i][j] == 1):
      queue.append((i,j))

while(queue):
  cury, curx = queue.pop()
  for dy, dx in directinos:
    ny, nx = cury + dy, curx + dx
    if(arr[ny][nx] == 0 and 0 < nx < M and 0 <= ny < N):
      queue.append((ny,nx))
      arr[ny][nx] = 1

print(arr)
