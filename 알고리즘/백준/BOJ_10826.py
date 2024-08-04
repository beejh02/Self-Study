import sys

n = int(sys.stdin.readline())
if(n == 0):
    print(0)
else:
    dp = [0 for i in range(n+1)]
    dp[0] = 0
    dp[1] = 1

    for i in range(2,n+1):
        dp[i] = dp[i-2]+dp[i-1]

    sys.stdout.write(str(dp[-1]))