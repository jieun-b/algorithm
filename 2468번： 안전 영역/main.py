#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 2468                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: jieunb_b <boj.kr/u/jieunb_b>                +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/2468                           #+#        #+#      #+#     #
#    Solved: 2025/02/14 23:35:20 by jieunb_b      ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
from collections import deque

input = sys.stdin.readline

n = int(input())

maxnum = 0
graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))
    for j in range(n):
        maxnum = max(maxnum, graph[i][j])

dy, dx = [0,1,0,-1], [1,0,-1,0]

def search(i, j, k, visited):
    queue = deque([(i, j)])
    visited[i][j] = True
    while queue:
        y, x = queue.popleft()
        for idx in range(4):
            new_y = y + dy[idx]
            new_x = x + dx[idx]
            if 0<=new_y<n and 0<=new_x<n:
                if graph[new_y][new_x] > k and not visited[new_y][new_x]:
                    visited[new_y][new_x] = True
                    queue.append((new_y, new_x))

result = 0
for k in range(maxnum):
    visited = [[False] * n for _ in range(n)]
    count = 0
    for i in range(n):
        for j in range(n):
            if graph[i][j] > k and not visited[i][j]:
                search(i, j, k, visited)
                count += 1
    result = max(result, count)
print(result)