def solution(s):
    stack = []
    answer = True
    
    for i in s:
        if(i == "("):
            stack.append(i)
        else:
            try:
                stack.pop()
            except:
                answer = False
                break
    if(stack):
        answer = False
        return answer
    else:
        return answer