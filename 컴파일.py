from collections import deque

N, M = map(int,input().split())

queue = deque([N])
arr = [0 for i in range(200001)]
arr[N] = 1
cnt = 0

while(queue):
    for i in range(len(queue)):
        x = queue.popleft()
        if(x == M):
            print(cnt)
            exit()
        for nx in (x-1, x+1, x*2):
            if(0 < nx <= 200000 and arr[nx] == 0):
                arr[nx] = 1
                queue.append(nx)
    cnt += 1

print(cnt)