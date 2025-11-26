def solution(n, computers):
    answer = 0
    visited = [False] * n

    def search(i):
        for j in range(n):
            if computers[i][j] == 1 and not visited[j]:
                visited[j] = True
                search(j)

    for i in range(n):
        if not visited[i]:     
            visited[i] = True
            search(i)
            answer += 1

    return answer