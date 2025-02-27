# 미로 탈출
from collections import deque

n, m = map(int, input().split())

graph = []
for _ in range(n):
    graph.append(list(map(int, input())))

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def bfs(y,x):
    queue = deque()
    queue.append((y,x))
    while queue:
        y, x = queue.popleft()
        for k in range(4):
            ny = y+dy[k]
            nx = x+dx[k]
            if 0 <= ny < n and 0 <= nx < m and graph[ny][nx] == 1:
                queue.append((ny, nx))
                graph[ny][nx] = graph[y][x] + 1
                
    return graph[n-1][m-1]

print(bfs(0,0))