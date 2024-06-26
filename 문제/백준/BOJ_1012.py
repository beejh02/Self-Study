from collections import deque

play = int(input())
result = []
for t in range(play):
    M, N, K = map(int,input().split())
    queue = deque()
    arr = [[0 for i in range(M)] for i in range(N)]

    for i in range(K):
        x, y = map(int,input().split())
        arr[y][x] = 1

    directions = [(-1,0), (0,1), (1,0), (0,-1)]
    cnt = 0

    for i in range(M):
        for j in range(N):
            if(arr[j][i] == 1):
                queue.append((j,i))
                while(queue):
                    cury, curx = queue.popleft()
                    arr[cury][curx] = 0
                    for dy, dx in directions:
                        ny = dy+cury
                        nx = dx+curx
                        if(0 <= ny < N and 0 <= nx < M and arr[ny][nx] == 1):
                            queue.append((ny,nx))
                            arr[ny][nx] = 0
                cnt += 1

    result.append(cnt)

for x in result:
    print(x)