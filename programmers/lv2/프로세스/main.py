def solution(priorities, location):
    answer = 0
    
    prior = []  # 우선 순위 확인용
    queue = []
    for i in range(len(priorities)):
        prior.append(priorities[i])
        queue.append((priorities[i], i))
    prior.sort(reverse=True)
    cnt = 1
    while queue:
        if queue[0][0] < prior[0]:
            queue.append(queue[0])
            queue = queue[1:]
            continue
        if location == queue[0][1]:
            return cnt
        queue = queue[1:]
        prior = prior[1:]
        cnt += 1
    
            