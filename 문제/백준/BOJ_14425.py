N, M = map(int,input().split())

table = {}
cnt = 0

for i in range(N):
    key = input()
    table[key] = 1

for i in range(M):
    key = input()
    try:
        cnt += table[key]
    except:
        pass

print(cnt)
