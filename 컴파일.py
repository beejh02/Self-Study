arr = [1,10,5,8,7,6,4,3,2,9]

for i in range(len(arr)):
    find = i
    for j in range(i+1, len(arr)):
        if(arr[j] < arr[find]):
            find = j
    arr[i], arr[find] = arr[find], arr[i]
    print(arr)