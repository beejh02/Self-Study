import sys

N = int(sys.stdin.readline())

dp = [0 for i in range(N+1)]

if (N == 1):
    print(4)
elif(N == 2):
    print(6)
else:
    dp[0] = 1
    dp[1] = 1

    for i in range(2,N+1):
        dp[i] = dp[i-1] + dp[i-2]

    print(dp[-2]*4 + dp[-3]*2)