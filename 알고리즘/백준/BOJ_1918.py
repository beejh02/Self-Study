string = input()

priority = {"*" : 3, "/" : 3, "+" : 2, "-" : 2, "(" : 1}
stack = []
result = ""

for i in string:
    if(i == "("):
        stack.append(i)
    elif(i == ")"):
        top = stack.pop()
        while(top != "("):
            result += top
            top = stack.pop()
    elif(i.isalpha()):
        result += i
    else:
        while((stack) and (priority[stack[-1]] >= priority[i])):
            result += stack.pop()
        stack.append(i)

while(stack):
    result += stack.pop()

print(result)