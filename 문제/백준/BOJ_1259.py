while(1):
    string = input()
    if(string == "0"):
        break
    compare = string[::-1]
    
    if(string == compare):
        print("yes")
    else:
        print("no")