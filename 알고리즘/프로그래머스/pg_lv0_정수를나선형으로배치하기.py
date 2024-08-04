def solution(n):
    arr = [[0 for i in range(n)] for i in range(n)]
    x = 0
    y = 0
    direction = 1
    
    
    for num in range(1, n*n+1) :
        arr[x][y] = num
        
        if direction == 1:
            if y == (n-1) or arr[x][y + 1] != 0:
                direction = 2
                x += 1
            else :
                y += 1
            
        elif direction == 2:
            if x == (n-1) or arr[x + 1][y] != 0:
                direction = 3
                y -= 1
            else :
                x += 1
        
        elif direction == 3:
            if x == 0 or arr[x][y - 1] != 0:
                direction = 4
                x -= 1
            else :
                y -= 1
                
        elif direction == 4 : 
            if x == 0 or arr[x - 1][y] != 0:
                direction = 1
                y += 1
            else :
                x -= 1
                
                
    return arr