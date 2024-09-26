import sys

n, m = map(int,sys.stdin.readline().split())
arr = []

def backtracking():
    if(len(arr) == m):
        print(" ".join(map(str, arr)))
        return
    
    for i in range(1, n+1):
        if(i not in arr):
            arr.append(i)
            backtracking()
            arr.pop()

backtracking()