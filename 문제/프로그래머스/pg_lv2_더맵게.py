import heapq

def solution(scoville, K):

    cnt = 0
    heapq.heapify(scoville)


    while(scoville[0] < K):
        try:
            n1 = heapq.heappop(scoville)
            n2 = heapq.heappop(scoville)*2

            heapq.heappush(scoville, n1+n2)
            cnt += 1
        except:
            return -1

    return cnt