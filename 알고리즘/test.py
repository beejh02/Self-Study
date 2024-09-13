from collections import deque
# import sys
# input = sys.stdin.readline
 
def solve(n, m, board):
    queue = deque()
    for i in range(m):
        for j in range(n):
            if board[i][j] == 1: queue.append([i, j, 0]) # x, y, 시간
    # 동 남 서 북
    dxs = (0, 1, 0, -1)
    dys = (1, 0, -1, 0)
 
    while queue:
        x, y, t = queue.popleft()
        T = t
        for dx, dy in zip(dxs, dys):
            nx, ny = x+dx, y+dy
            if nx<0 or nx>=m or ny<0 or ny>=n: continue
            if board[nx][ny] == 0:
                board[nx][ny] = 1
                queue.append([nx, ny, t+1])
    for i in range(m):
        for j in range(n):
            if board[i][j] == 0:
                return -1
    return T
 
 
if __name__ == '__main__':
    n, m = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(m)]
    print(solve(n, m, board))