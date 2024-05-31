import heapq

arr = [1, 2, 3, 9, 10, 12]
K = 7
cnt = 0
heapq.heapify(arr)


while(min(arr) < 7):

    n1 = heapq.heappop(arr)
    n2 = heapq.heappop(arr)*2

    heapq.heappush(arr, n1+n2)
    cnt += 1

print(arr)
print(cnt)