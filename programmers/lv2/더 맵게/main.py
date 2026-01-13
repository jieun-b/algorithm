import heapq
def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    while True:
        first = heapq.heappop(scoville)
        if first >= K:
            return answer
        if scoville != []:
            second = heapq.heappop(scoville)
            heapq.heappush(scoville, (first + second*2))
            answer += 1
        else:
            return -1