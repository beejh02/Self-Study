import sys

n = int(sys.stdin.readline())

a = 1
cnt = 0

for i in range(2, n+1):
    a *= i

a = str(a)[::-1]

for i in a:
    if(i == "0"):
        cnt += 1
    else:
        sys.stdout.write(str(cnt))
        break