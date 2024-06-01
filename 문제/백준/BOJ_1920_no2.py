n = int(input())
arr = sorted(list(map(int,input().split())))
n = int(input())
ser = list(map(int,input().split()))

def find(finding):
    left = 0
    right = len(arr)-1

    while(left < right):
        mid = (left + right) // 2
        if(arr[mid] >= finding):
            right = mid
        else:
            left = mid+1
    if(arr[left] == finding):
        return 1

for i in ser:
    if(find(i) == None):
        print(0)
    else:
        print(find(i))