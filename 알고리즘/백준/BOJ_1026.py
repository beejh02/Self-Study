n = int(input())

a = list(map(int,input().split()))
b = list(map(int,input().split()))

cnt = 0

a.sort()
b.sort(reverse = True)

for i in range(len(a)):
    cnt += a[i]*b[i]
    
print(cnt)