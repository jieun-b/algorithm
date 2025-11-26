from collections import deque

def solution(maps):
    answer = 0
    visited = [[-1]*len(maps[0]) for _ in range(len(maps))]
    
    dr = [1, -1, 0, 0]
    dc = [0, 0, 1, -1]
    
    def search():
        queue = deque([(0,0)])
        visited[0][0] = 1
        while queue:
            r, c = queue.popleft()
            for k in range(4):
                n_r, n_c = r+dr[k], c+dc[k]
                if 0<=n_r<len(maps) and 0<=n_c<len(maps[0]):
                    if maps[n_r][n_c] == 1 and visited[n_r][n_c] == -1:
                        queue.append((n_r, n_c))
                        visited[n_r][n_c] = visited[r][c] + 1
    
    search()
    
    return visited[-1][-1]