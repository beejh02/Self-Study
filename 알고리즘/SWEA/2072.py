T = int(input())

for i in range(T):
    result = []
    arr = list(map(int, input().split()))
    
    for j in arr:
        if j % 2 == 1:
            result.append(j)

    answer = f"#{i + 1} {sum(result)}"
    print(answer)