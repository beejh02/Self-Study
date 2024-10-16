T = int(input())

for i in range(T):
    x, y, z = map(int,input().split())
    cnt = 0
    while(max(x,y) <= z):
        cnt += 1
        if(x >= y):
            y += x
        else:
            x += y


    print(cnt)