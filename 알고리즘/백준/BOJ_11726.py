import sys

n = int(sys.stdin.readline())

if(n == 1):
    print(1)
elif(n == 2):
    print(2)
else:
    dp = [0 for i in range(n)]

    dp[0] = 1
    dp[1] = 2

    for i in range(2,n):
        dp[i] = dp[i-1] + dp[i-2]

    print(dp[-1]%10007)