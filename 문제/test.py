n = int(input())

n1 = 1
n2 = 2

cnt = 2

if(n != 1):
    while(n > cnt):
        cnt += 1
        
        tmp1 = n2
        tmp2 = (n1+n2)%10007
        
        n1 = tmp1
        n2 = tmp2
        
    print(n2 % 10007)
else:
    print(1)