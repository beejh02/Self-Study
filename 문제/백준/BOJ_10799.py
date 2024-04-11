string = input()
stack = []
cnt = 0

for i in string:
    if(i == "("):
        stack.append(i)
    else:
        if(stack[-1]=="("):
            stack.pop()
            cnt += len(stack)
        else:
            stack.pop()
            cnt += 1
            
print(cnt)