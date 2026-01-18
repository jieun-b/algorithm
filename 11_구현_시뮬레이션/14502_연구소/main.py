#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 14502                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: jieunb_b <boj.kr/u/jieunb_b>                +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/14502                          #+#        #+#      #+#     #
#    Solved: 2026/01/18 22:06:41 by jieunb_b      ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
graph = []
walls = []
viruses = []
for i in range(n):
    tmp = list(map(int, input().split()))
    for j in range(m):
        if tmp[j] == 2:
            viruses.append((i, j))
    graph.append(tmp)

dr = [1, 0, -1, 0]
dc = [0, 1, 0, -1]

def count(graph):
    visited = [[False]*m for _ in range(n)]
    for i, j in viruses:
        queue = deque([(i, j)])
        visited[i][j] = True
        while queue:
            r, c = queue.popleft()
            for k in range(4):
                nr, nc = r+dr[k], c+dc[k]
                if 0<=nr<n and 0<=nc<m:
                    if not visited[nr][nc] and graph[nr][nc] == 0:
                        queue.append((nr, nc))
                        visited[nr][nc] = True
                        graph[nr][nc] = 2
    cnt = 0
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                cnt += 1
    return cnt

def choice():
    global max_cnt
    if len(walls) == 3:
        new_graph = [row[:] for row in graph]
        for i, j in walls:
            new_graph[i][j] = 1
        new_cnt = count(new_graph)
        max_cnt = max(max_cnt, new_cnt)
        return
    if walls:
        r, c = walls[-1]
        for i in range(r, n):
            for j in range(m):
                if i == r and j <= c: 
                    continue
                if graph[i][j] == 0:
                    walls.append((i, j))
                    choice()
                    walls.pop()
    else: 
        for i in range(n):
            for j in range(m):
                if graph[i][j] == 0:
                    walls.append((i, j))
                    choice()
                    walls.pop()
max_cnt = 0
choice()
print(max_cnt)