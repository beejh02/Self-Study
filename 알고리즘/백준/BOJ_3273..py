import sys

n = int(sys.stdin.readline())
arr = list(map(int,sys.stdin.readline().split()))
arr.sort()
x = int(sys.stdin.readline())

left = 0
right = n - 1
result = 0

while(left < right):
    value = arr[left] + arr[right]
    if(value == x):
        result += 1
        left += 1
    elif(value < x):
        left += 1
    else:
        right -= 1

print(result)