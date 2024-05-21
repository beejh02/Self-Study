a,b = map(int,input().split())

resulta = True
resultb = True

if(a == 0 or a == 2 or a == 5):
    pass
else:
    resulta = False
if(b == 0 or b == 2 or b == 5):
    pass
else:
    resultb = False

if(a == 0 and b == 2):
    print(">")
elif(a == 0 and b == 5):
    print("<")
elif(a == 0 and b == 0):
    print("=")
elif(a == 2 and b == 0):
    print("<")
elif(a == 2 and b == 2):
    print("=")
elif(a == 2 and b == 5):
    print(">")
elif(a == 5 and b == 0):
    print(">")
elif(a == 5 and b == 2):
    print("<")
elif(a == 5 and b == 5):
    print("=")
else:
    if(resulta == False and resultb == False):
        print("=")
    elif(resulta == False):
        print("<")
    elif(resultb == False):
        print(">")