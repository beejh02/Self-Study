while(1):
    arr = list(map(int,input().split()))
    if(sum(arr) != 180):
        print("Invalid")
    elif(arr[0] == 0 and arr[1] == 0 and arr[2] == 0):
        break
    elif(arr[0] == arr[1] == arr[2]):
        print("Equilateral")
    elif(arr[0] == arr[1] or arr[1] == arr[2] or arr[0] == arr[2]):
        print("Isosceles")
    else:
        print("Scalene") 