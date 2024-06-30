from collections import deque

queue = deque()
result = []

directions = [(-1,0), (0,1), (1,0), (0,-1)]

while(1):
    w, h = map(int,input().split())
    if(w == 0 and h == 0):
        break
    else:
        arr = []
        cnt = 0

        for i in range(h):
            arr.append(list(map(int,input().split())))

        for i in range(h):
            for j in range(w):
                if(arr[i][j] == 1):
                    queue.append((i,j))
                    while(queue):
                        cury, curx  = queue.popleft()
                        arr[cury][curx] = 0
                        for dy, dx in directions:
                            ny, nx = cury + dy, curx + dx
                            if(0 <= ny < h and 0 <= nx < w and arr[ny][nx] == 1):
                                queue.append((ny,nx))

                    cnt += 1

    result.append(cnt)
print(result)