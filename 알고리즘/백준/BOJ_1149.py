N = int(input())

arr = []

for i in range(N):
    arr.append(list(map(int,input().split())))
    
for i in range(1, len(arr)):
    arr[i][0] = min(arr[i-1][1],arr[i-1][2])+arr[i][0]
    arr[i][1] = min(arr[i-1][0],arr[i-1][2])+arr[i][1]
    arr[i][2] = min(arr[i-1][0],arr[i-1][1])+arr[i][2]

a = arr[N-1][0]
b = arr[N-1][1]
c = arr[N-1][2]

print(min(a,b,c))