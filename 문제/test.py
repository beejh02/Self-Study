arr = list(map(int,input().split()))

arr.sort()

print(arr)
if(arr[0]+arr[1] > arr[2]):
    print(sum(arr))
else:
    print((arr[0]+arr[1])*2-1)