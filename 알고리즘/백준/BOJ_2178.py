from collections import deque

def bfs(maze, n, m):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    queue = deque([(0, 0)])
    maze[0][0] = 1
    
    while queue:
        x, y = queue.popleft()
        
        if x == n - 1 and y == m - 1:
            return maze[x][y]
        
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            
            if 0 <= nx < n and 0 <= ny < m and maze[nx][ny] == 1:
                queue.append((nx, ny))
                maze[nx][ny] = maze[x][y] + 1
    
    return -1
n, m = map(int, input().split())

maze = []
for i in range(n):
     maze.append(list(map(int, input())))

print(bfs(maze, n, m))