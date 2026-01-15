import heapq
def solution(jobs):
    answer = 0
    queue = []
    now = 0
    prev = -1
    done = 0
    while done < len(jobs):
        # 현재 시점에서 큐에 넣을 수 있는 작업    
        for job in jobs:
            if prev < job[0] <= now:
                heapq.heappush(queue, [job[1], job[0]])
        # 큐에 있는 작업 실행
        if queue:
            long, start = heapq.heappop(queue)
            prev = now
            now += long
            answer += (now - start)
            done += 1
        else:
            now += 1
    return answer//len(jobs)