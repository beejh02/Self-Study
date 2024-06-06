import sys

N, M = map(int,sys.stdin.readline().split())

arr = list(map(int,sys.stdin.readline().split()))

left = 0
right = 0
result = 0

while(left <= right and right <= N):
    value = sum(arr[left:right])

    if(value == M):
        result += 1
        left += 1
    elif(value < M):
        right += 1
    else:
        left += 1

sys.stdout.write(str(result))