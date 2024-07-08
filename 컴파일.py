from collections import deque

n, m = map(int, input().split())
arr = []
queue = deque()
directions = [(-1, 0), (0, 1), (0, -1), (1, 0)]
visited = [[0 for i in range(m)] for i in range(n)]

for i in range(n):
    arr.append(list(map(int, input())))

queue.append((0, 0))
visited[0][0] = 1

while queue:
    cury, curx = queue.popleft()
    
    for dy, dx in directions:
        ny = dy + cury
        nx = dx + curx
        
        if 0 <= ny < n and 0 <= nx < m and arr[ny][nx] == 1 and visited[ny][nx] == 0:
            visited[ny][nx] = visited[cury][curx] + 1
            queue.append((ny, nx))
            
            if ny == n - 1 and nx == m - 1:
                print(visited[ny][nx])
                break