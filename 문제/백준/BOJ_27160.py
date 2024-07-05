import sys

n = int(sys.stdin.readline())

S = ["STRAWBERRY", "BANANA", "LIME", "PLUM"]
cnt = [0,0,0,0]

for i in range(n):
    fruit, num = map(str,sys.stdin.readline().split())
    for j in range(len(S)):
        if(S[j]==fruit):
            cnt[j] += int(num)

if(5 in cnt):
    sys.stdout.write("YES")
else:
    sys.stdout.write("NO")