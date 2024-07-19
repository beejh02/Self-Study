N = int(input())
arr = list(map(int,input().split()))

dp = [1 for i in range(len(arr))]

for i in range(N):
    for j in range(i):
        if(arr[i] > arr[j]):
            if(dp[i] < dp[j]+1):
                dp[i] = dp[j]+1

print(max(dp))