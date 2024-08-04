N, K = map(int,input().split())
arr = []

for i in range(N, N*K+1, N):
    arr.append(int(str(i)[::-1]))

print(max(arr))
