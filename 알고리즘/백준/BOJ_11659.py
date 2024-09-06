import sys

N, M = map(int,sys.stdin.readline().split())

arr = list(map(int,sys.stdin.readline().split()))
psum = [0 for i in range(1, N+2)]
temp = 0

for i in range(1,N+1):
    temp += arr[i-1]
    psum[i] = temp

for i in range(M):
    start, end = map(int,sys.stdin.readline().split())
    print(psum[end] - psum[start-1])