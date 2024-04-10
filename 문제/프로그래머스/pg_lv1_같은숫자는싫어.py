def solution(arr):
    stack = []
    answer = []
    answer.append(arr[0])


    for i in arr:
        if(stack):
            curr = stack.pop()
            if(curr != i):
                answer.append(i)

        stack.append(i)

    return answer