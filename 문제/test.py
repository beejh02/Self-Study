import sys
n = int(input())

arr = []
arr.append(list(map(int, sys.stdin.readline().split())))
result = arr.copy()

for i in range(1,n):
    arr.append(list(map(int, sys.stdin.readline().split())))
    result.append([0]*(i+1))
    for k in range(i):
        result[i][k] = max(result[i][k], result[i-1][k] + arr[i][k])
        result[i][k+1] = max(result[i][k+1], result[i-1][k] + arr[i][k+1])

print(max(result[n-1]))