arr = [1,2,3,4,5,6,7,8,9]
copy = [1,2,3,4,5,6,7,8,9]
result = []

left = 0
right = len(arr)-1

while(1):
    mid = (left + right) // 2

    result.append(sum(copy[:mid]))
    copy = copy[mid+1:]
    left = copy[0]
    print(copy)
    print(result)