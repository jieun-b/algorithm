#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 1926                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: jieunb_b <boj.kr/u/jieunb_b>                +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/1926                           #+#        #+#      #+#     #
#    Solved: 2025/02/13 11:05:38 by jieunb_b      ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))
visited = [[0 for _ in range(m)] for _ in range(n)]

def search(i, j):
    queue = deque([(i, j)])
    count = 1
    visited[i][j] += count
    while queue:
        y, x = queue.popleft()
        for idx in range(4):
            new_y = y + dy[idx]
            new_x = x + dx[idx]
            if 0<=new_y<n and 0<=new_x<m:
                if graph[new_y][new_x]==1 and visited[new_y][new_x]==0:
                    queue.append((new_y, new_x))
                    count += 1
                    visited[new_y][new_x] += count
    return count

dx = [1,0,-1,0]
dy = [0,1,0,-1]

num = 0
width = 0
for i in range(n):
    for j in range(m):
        if graph[i][j]==1 and visited[i][j]==0:
            count = search(i, j)
            num += 1
            width = max(width, count)
print(num)
print(width)



# import sys
# from collections import deque

# input = sys.stdin.readline
# dx, dy = [1, 0, -1, 0], [0, 1, 0, -1]

# n, m = map(int, input().split())
# graph = [list(map(int, input().split())) for _ in range(n)]
# visited = [[0] * m for _ in range(n)]

# def search(i, j):
#     queue = deque([(i, j)])
#     visited[i][j] = 1
#     count = 1
#     while queue:
#         y, x = queue.popleft()
#         for idx in range(4):
#             ny, nx = y + dy[idx], x + dx[idx]
#             if 0 <= ny < n and 0 <= nx < m and graph[ny][nx] == 1 and not visited[ny][nx]:
#                 queue.append((ny, nx))
#                 visited[ny][nx] = 1
#                 count += 1
#     return count

# num, width = 0, 0
# for i in range(n):
#     for j in range(m):
#         if graph[i][j] == 1 and not visited[i][j]:
#             width = max(width, search(i, j))
#             num += 1

# print(num, width, sep="\n")
