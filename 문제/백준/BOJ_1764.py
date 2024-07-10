import sys
n, m = map(int, sys.stdin.readline().split())


arrn = set()
for i in range(n):
    arrn.add(sys.stdin.readline())

arrm = set()
for i in range(m):
    arrm.add(sys.stdin.readline())


result = sorted(arrn & arrm)


print(len(result))
for i in result:
    sys.stdout.write(i)