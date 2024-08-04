#N = 문서의 개수
#M = queue의 몇번째에 놓여있는지 Check
from collections import deque

play = int(input())

for i in range(play):
    N, M = map(int,input().split())
    queue = deque(list(map(int,input().split())))
    cnt = 1
    while(1):
        if(queue[0] >= max(queue)):
            if(M == 0):
                print(cnt)
                break
            queue.popleft()
            cnt += 1
            M -= 1
            if(M < 0): M = len(queue) - 1
        else:
            queue.append(queue.popleft())
            M -= 1
            if (M < 0): M = len(queue)-1