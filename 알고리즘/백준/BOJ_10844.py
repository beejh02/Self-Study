import sys

n = int(sys.stdin.readline())

dp = [[0 for i in range(10)] for j in range(101)]

for i in range(1, 10):
    dp[1][i] = 1

for i in range(2, n + 1):
    for j in range(10):
        if j > 0:
            dp[i][j] += dp[i - 1][j - 1]
        if j < 9:
            dp[i][j] += dp[i - 1][j + 1]

sys.stdout.write(str(sum(dp[n]) % 1000000000))