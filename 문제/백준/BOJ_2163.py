import sys

N, M = map(int,sys.stdin.readline().split())

sys.stdout.write(str((N-1) * M + (M-1)))