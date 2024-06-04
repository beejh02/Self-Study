n = int(input())
x, y = map(int,input().split())
cnt = 0

if(n == 1):
    print(0)
else:
    if(x == 1 or x == n):
        cnt += 1
    if(y == 1 or y == n):
        cnt += 1
    
    print(4-cnt)