N, M = map(int,input().split())

dict = {}

for i in range(N):
    key, value = map(str,input().split())
    dict[key] = value

for i in range(M):
    print(dict[str(input())])