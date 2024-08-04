import sys

n = sys.stdin.readline()
arr = list(map(int,sys.stdin.readline().split()))
m = sys.stdin.readline()
ser = list(map(int,sys.stdin.readline().split()))
table = {}

for index, value in enumerate(arr):
    table[value] = index

for i in ser:
    try:
        if(table[i] < len(ser)):
            print(1)
    except:
        print(0)


## 해시테이블(table) 만들어서 딕셔너리로 빠른탐색