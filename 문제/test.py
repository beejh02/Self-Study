import sys

setting = sys.stdin.readline()
n = int(input())
index = len(setting)

for i in range(n):
    enter = list(map(str,sys.stdin.readline().split()))
    if(enter[0] == 'L'):
        if(index == 0):
            continue
        else:
            index -= 1
    elif(enter[0] == 'D'):
        if(index == len(setting)):
            continue
        else:
            index += 1
    elif(enter[0] == 'B'):
        if(index == 0):
            continue
        else:
            setting = setting[:index-1] + setting[index:]
            index -= 1
    else:
        if(index == 0):
            setting = enter[1] + setting
            index += 1
        else:
            setting = setting[:index] + enter[1] + setting[index:]
            index += 1

sys.stdout.write(setting.replace("\n", ""))