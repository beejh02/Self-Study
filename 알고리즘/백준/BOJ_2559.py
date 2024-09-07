import sys

N, K = map(int,sys.stdin.readline().split())

arr = list(map(int,sys.stdin.readline().split()))

psum = [0 for i in range(N)]
temp = 0
result = []
answer = []
start, end = 0, K

for i in range(N):
    temp += arr[i]
    psum[i] = temp

answer.append(psum[K-1])

for i in range(N-K):
    answer.append(psum[end] - psum[start])
    start += 1
    end += 1

print(max(answer))