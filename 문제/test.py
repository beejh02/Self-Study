import heapq

n = int(input())

heap = []
result = []

for i in range(n):
    value = int(input())
    if(value != 0):
        heapq.heappush(heap, (abs(value), value))
    else:
        if(heap):
            result.append(heapq.heappop(heap)[1])
        else:
            result.append(0)

print(result)