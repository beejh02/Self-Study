import heapq

operations = ["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"]

max_heapq = []
min_heapq = []
setting = {}

for i in operations:
    if(i.split()[0] == 'I'):
        num = i.split()[1]
        heapq.heappush(max_heapq, int(num))
        heapq.heappush(min_heapq, -int(num))
        setting[num] = setting.get(num, 0) + 1
    else:
        if(i[2] == '-'):
            heapq.heappop(min_heapq)
        else:
            heapq.heappop(max_heapq)

print(max_heapq)
print(min_heapq)
