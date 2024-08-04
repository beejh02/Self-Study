while(1):
    stack = []
    answer = True
    string = input()
    if(string == "."):
        break
    
    for i in range(len(string)):
        try:
            if(string[i] == "(" or string[i] == "["):
                stack.append(string[i])
            elif(string[i] == ")"):
                if(stack[-1] == "("):
                    stack.pop()
                else:
                    answer = False
            elif(string[i] == "]"):
                if(stack[-1] == "["):
                    stack.pop()
                else:
                    answer = False
        except:
            answer = False
    if(stack):
        answer = False
    if(answer):
        print("yes")
    else:
        print("no")