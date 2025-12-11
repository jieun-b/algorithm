from collections import deque

def solution(begin, target, words):
    def check(a, b):
        diff = 0
        for i in range(len(a)):
            if a[i] != b[i]:
                diff += 1
        if diff == 1:
            return True
        else:
            return False
        
    queue = deque([(begin, 0)])
    visited = [False]*len(words)
    while queue:
        cur, step = queue.popleft()
        if cur == target:
            return step
        for i in range(len(words)):
            if not visited[i] and check(words[i], cur):
                queue.append((words[i], step+1))
                visited[i] = True 
    return 0