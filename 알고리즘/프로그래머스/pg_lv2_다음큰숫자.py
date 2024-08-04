def solution(n):
    comp = n
    n2 = bin(n)[2:]

    while(1):
        comp += 1
        if(str(bin(comp)[2:]).count('1') == str(n2).count('1')):
            return comp