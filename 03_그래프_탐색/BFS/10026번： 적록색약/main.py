#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 10026                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: jieunb_b <boj.kr/u/jieunb_b>                +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/10026                          #+#        #+#      #+#     #
#    Solved: 2024/05/21 16:35:40 by jieunb_b      ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

from collections import deque

N = int(input())
mat = [list(input().strip()) for _ in range(N)]
dx = [0, 1, 0, -1] 
dy = [-1, 0, 1, 0]

def bfs(i, j):
    queue = deque()
    queue.append((i, j))
    visited[i][j] = 1
    while(queue):
        y, x = queue.popleft() 
        for k in range(4):
            ny = y + dy[k] 
            nx = x + dx[k]
            if 0<=ny<N and 0<=nx<N:
                if mat[y][x] == mat[ny][nx] and visited[ny][nx] == 0:
                    queue.append((ny, nx))
                    visited[ny][nx] = 1

visited = [[0] * N for _ in range(N)]          
count1 = 0
for i in range(N):
    for j in range(N):
        if visited[i][j] == 0:
            bfs(i, j)
            count1 += 1

for i in range(N):
    for j in range(N):
        if mat[i][j] == 'G':
            mat[i][j] = 'R'

visited = [[0] * N for _ in range(N)]   
count2 = 0
for i in range(N):
    for j in range(N):
        if visited[i][j] == 0:
            bfs(i, j)
            count2 += 1

print(count1, count2)