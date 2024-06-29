import sys
from collections import defaultdict

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
find = list(map(int, sys.stdin.readline().split()))

min_val = min(arr)
plus = -min_val if min_val < 0 else 0

key = defaultdict(int)

for num in arr:
    key[num + plus] += 1

for num in find:
    print(key[num + plus], end=" ")