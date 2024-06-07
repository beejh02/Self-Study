"""
2024-06-07 삽입정렬 하기

내용 :  list[index]값과 그다음으로 큰 값을 비교하여 삽입한 후
        그 이후엔 그 다음 인덱스 값이 그 사이에 비교연산후
        적절한 위치에 삽입하여 이미 정렬된 값에 삽입위치를 정하기에
        전체탐색보다는 효율적인 정렬방법이다.
"""

arr = [1,10,5,8,7,6,4,3,2,9]

for i in range(len(arr)-1):
    j = i
    while(arr[j] > arr[j+1]):
        temp = arr[j]
        arr[j] = arr[j+1]
        arr[j+1] = temp
        j -= 1

print(arr)