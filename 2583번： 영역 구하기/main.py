#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 2583                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: jieunb_b <boj.kr/u/jieunb_b>                +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/2583                           #+#        #+#      #+#     #
#    Solved: 2024/05/27 00:06:39 by jieunb_b      ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

from collections import deque

M, N, K = list(map(int, input().split()))
paper = [[False]*N for _ in range(M)]
visited = [[False]*N for _ in range(M)]

def painting(left_x, left_y, right_x, right_y):
    for i in range(left_y, right_y, -1):
        for j in range(left_x, right_x):
            paper[i][j] = True

def bfs(y, x):
    queue = deque()
    queue.append((y,x))
    result = 1
    visited[y][x] = True
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    while queue:
        y, x = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<N and 0<=ny<M and not paper[ny][nx] and not visited[ny][nx]:
                queue.append((ny, nx))
                result += 1
                visited[ny][nx] = True
    return result

for _ in range(K):
    left_x, left_y, right_x, right_y = list(map(int, input().split()))
    painting(left_x, M-1-left_y, right_x, M-1-right_y)

count = 0
results = []
for i in range(M):
    for j in range(N):
        if not paper[i][j] and visited[i][j] == 0:
            results.append(bfs(i, j))
            count += 1

print(count)
print(*sorted(results))