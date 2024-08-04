import sys

N, M = map(int,sys.stdin.readline().split())

dict = {}

for i in range(N):
    key, value = map(str,sys.stdin.readline().split())
    dict[key] = value

for i in range(M):
    print(dict[str(sys.stdin.readline().strip())])