#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 14940                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: jieunb_b <boj.kr/u/jieunb_b>                +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/14940                          #+#        #+#      #+#     #
#    Solved: 2025/04/23 22:26:17 by jieunb_b      ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
visited = [[-1] * m for _ in range(n)]
graph = []
for i in range(n):
    line = list(map(int, input().split()))
    for j in range(m):
        if line[j] == 2:
            target = (i, j)
        if line[j] == 0:
            visited[i][j] = 0
    graph.append(line)

# 목표지점에서 모든 거리 계산하기
dx = [1,0,-1,0]
dy = [0,1,0,-1]

def search(i,j):
    queue = deque()
    queue.append((i,j))
    visited[i][j] = 0
    while queue:
        y, x = queue.popleft()
        for k in range(4):
            new_y = y+dy[k]
            new_x = x+dx[k]
            if 0<=new_y<n and 0<=new_x<m:
                if graph[new_y][new_x] == 1 and visited[new_y][new_x] == -1:
                    visited[new_y][new_x] = visited[y][x] + 1
                    queue.append((new_y, new_x))

search(target[0], target[1])
for i in range(n):
    print(*visited[i])