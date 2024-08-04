from collections import deque

M, N = map(int,input().split())
arr = []
queue = deque()
cnt = 0

for i in range(N):
    arr.append(list(map(int,input().split())))

directions = [(-1,0), (0,1), (1,0), (0,-1)]

for i in range(M):
    for j in range(N):
        if(arr[j][i] == 1):
            queue.append((j,i))
            while(queue):
                cury, curx = queue.popleft()
                for dy, dx in directions:
                    ny = dy + cury
                    nx = dx + curx

                    if(0 <= ny < N and 0 <= nx < M and arr[ny][nx] == 0):
                        queue.append((ny,nx))
                        arr[ny][nx] = 1
                cnt += 1

print(cnt)