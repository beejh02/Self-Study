N = int(input())
bag = 0

while N >=0 :
    if N % 5 == 0:
        bag += N // 5
        break
    else:
        N  -= 3
        bag += 1
else:
    bag = -1

print(bag)