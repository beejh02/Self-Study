N = int(input())
arr = []
for i in range(1,N+1):
    arr.append(list(map(str,input().split())))
    print(f"Case #{i}: " + " ".join(arr[0][::-1]))
    arr = []