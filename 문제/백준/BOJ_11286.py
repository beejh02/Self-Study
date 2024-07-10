import heapq
import sys

n = int(sys.stdin.readline())

heap = []

for i in range(n):
    value = int(sys.stdin.readline())
    if(value != 0):
        heapq.heappush(heap, (abs(value), value))
    else:
        if(heap):
            print(heapq.heappop(heap)[1])
        else:
            print(0)