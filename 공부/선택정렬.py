"""
2024-06-07 선택정렬 하기

내용 :  list에서 제일 작은 값을 전체탐색으로 찾은 다음,
        list[0]~list[마지막]까지 순서대로 위치를 swap해줘서
        작은 값이 앞에오도록 정렬하는 방법
        반대로 정렬하고자 한대면 max값을 전체탐색으로 하면 된다.
"""

arr = [1,10,5,8,7,6,4,3,2,9]

for i in range(len(arr)):
    min = 999
    for j in range(i,len(arr)):
        if(min > arr[j]):
            min = arr[j]
            index = j
    temp = arr[i]
    arr[i] = arr[index]
    arr[index] = temp

    print(arr)