import sys

n = int(sys.stdin.readline())

arr = []
for i in range(n):
    a, b = map(str,sys.stdin.readline().split())
    arr.append([int(a), b])
    
arr = sorted(arr, key = lambda x : int(x[0]))

for age, name in arr:
    print(age, name)
    