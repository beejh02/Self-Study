import sys

N = int(sys.stdin.readline())

dp = [i%2 for i in range(1001)]

if(dp[N] == 0):
    sys.stdout.write("CY\n")
else:
    sys.stdout.write("SK\n")