string = input()
stack = []
cnt = 0

for i in range(len(string)):
    if(string[i] == "("):
        stack.append(string[i])
    else:
        if(string[i-1]=="("):
            stack.pop()
            cnt += len(stack)
        else:
            stack.pop()
            cnt += 1
            
print(cnt)