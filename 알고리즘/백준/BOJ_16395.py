n, k = map(int,input().split())

t = max(n,k)

if(n == 0 and k == 0):
    print(1)
elif(n == 1 and k == 0):
    print(1)
elif(n == 1 and k == 1):
    print(1)
else:
    arr = [[0 for i in range(t)] for i in range(t)]

    arr[0][0] = 1
    arr[1][0] = 1
    arr[1][1] = 1

    for i in range(2, t):
        for j in range(t):
            if(j == 0):
                arr[i][j] = 1
            else:
                arr[i][j] = arr[i-1][j-1] + arr[i-1][j]

        print(arr[n-1][k-1])