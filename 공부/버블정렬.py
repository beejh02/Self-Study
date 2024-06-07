"""
2024-06-07 버블정렬 하기

내용 :  list에서 반복문을 통하여 list[i]와 list[i+1] 의 크기를 비교하여
        list[i]>list[i+1]이라면 둘의 위치를 바꿔주어 최종적으로 한번 순회시
        최대값이 맨뒤로 가게되는 정렬방법 이것은 len(arr) 횟수만큼 반복하면
        모든 값들이 오름차순으로 정렬되게 된다.

"""

arr = [1,10,5,8,7,6,4,3,2,9]

for j in range(len(arr)):
    for i in range(len(arr)-1):
        if(arr[i] > arr[i+1]):
            temp = arr[i]
            arr[i] = arr[i+1]
            arr[i+1] = temp

print(arr)