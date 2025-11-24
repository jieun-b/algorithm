def solution(k, dungeons):
    answer = -1
    visited = [False] * len(dungeons)
    
    def search(cur, idx):
        nonlocal answer
        for i in range(len(dungeons)):
            need, reduce = dungeons[i][0], dungeons[i][1]
            if need <= cur and not visited[i]: 
                visited[i] = True
                search(cur-reduce, idx+1)
                visited[i] = False
        answer = max(answer, idx)
    
    search(k, 0)
    return answer