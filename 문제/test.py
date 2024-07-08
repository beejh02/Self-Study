from collections import deque

n, m = map(int,input().split())
arr = []
queue = deque()
directions = [(-1,0), (0,1), (0,-1), (1,0)]
cnt = 0
visited = [[0 for i in range(m)] for i in range(n)]

for i in range(n):
    arr.append(list(map(int,input())))

queue.append((0,0))
while(queue):
    cury, curx = queue.popleft()

    for dy, dx in directions:
        ny = dy + cury
        nx = dx + curx
        
        if(0 <= ny < n and 0 <= nx < m and arr[ny][nx] == 1 and visited[ny][nx] == 0):
            visited[ny][nx] = 1
            queue.append([ny,nx])
            cnt += 1
print(cnt-1)