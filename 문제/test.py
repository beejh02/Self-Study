n = int(input())
temp = n
i = 2

while(i <= n):
    if(temp % i == 0):
        print(i)
        temp //= i
    else:
        i += 1