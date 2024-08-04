n = int(input())
arr = [int(input()) for i in range(n)]
if(n == 1):
    print(arr[0])
elif(n == 2):
    print(arr[0]+arr[1])
else:
    dp = [[0]*(n+1) for i in range(2)]

    dp[1][1] = arr[0]
    dp[0][2] = arr[0]+ arr[1]
    dp[1][2] = arr[1]

    for i in range(3, n+1):
        dp[0][i] = dp[1][i-1] + arr[i-1]
        dp[1][i] = max(dp[0][i-2], dp[1][i-2]) + arr[i-1]

    print(max(dp[0][n], dp[1][n]))