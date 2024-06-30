def dfs(x, y, h, w, graph, visited):
    # 8방향 정의 (상, 하, 좌, 우, 좌상, 우상, 좌하, 우하)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
    stack = [(x, y)]
    visited[x][y] = True
    
    while stack:
        cx, cy = stack.pop()
        for dx, dy in directions:
            nx, ny = cx + dx, cy + dy
            if 0 <= nx < h and 0 <= ny < w and not visited[nx][ny] and graph[nx][ny] == 1:
                visited[nx][ny] = True
                stack.append((nx, ny))

def count_islands(w, h, graph):
    visited = [[False] * w for _ in range(h)]
    count = 0
    
    for i in range(h):
        for j in range(w):
            if graph[i][j] == 1 and not visited[i][j]:
                dfs(i, j, h, w, graph, visited)
                count += 1
    return count

while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    graph = [list(map(int, input().split())) for _ in range(h)]
    print(count_islands(w, h, graph))
