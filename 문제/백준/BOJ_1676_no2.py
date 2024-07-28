import sys

n = int(sys.stdin.readline())

a = n//5
b = n//25
c = n//125

sys.stdout.write(str(a+b+c))