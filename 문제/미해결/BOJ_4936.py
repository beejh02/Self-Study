from collections import deque

queue = deque()

directions = [(-1,0), (0,1), (1,0), (0,-1)]

w, h = map(int,input().split())
arr = []

for i in range(h):
    arr.append(list(map(int,input().split())))

for i in arr:
    print(i)

for i in range(w):
    for j in range(h):
        for dx, dy in directions:
            
        arr[j][i]