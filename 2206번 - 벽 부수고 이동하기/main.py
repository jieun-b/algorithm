#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 2206                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: jieunb_b <boj.kr/u/jieunb_b>                +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/2206                           #+#        #+#      #+#     #
#    Solved: 2025/06/12 21:46:04 by jieunb_b      ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
graph = []
for _ in range(n):
    row = list(input().strip()) 
    graph.append(list(map(int, row)))
visited = [[[0]*2 for _ in range(m)] for _ in range(n)]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def search():
    queue = deque([(0, 0, 0)])
    visited[0][0][0] = 1
    while(queue):
        y, x, visit = queue.popleft()
        for k in range(4):
            new_y = y + dy[k]
            new_x = x + dx[k]
            if 0<=new_y<n and 0<=new_x<m:
                if graph[new_y][new_x] == 0 and visited[new_y][new_x][visit] == 0:
                    queue.append((new_y, new_x, visit))
                    visited[new_y][new_x][visit] = visited[y][x][visit] + 1
                if graph[new_y][new_x] == 1 and visit == 0:
                    queue.append((new_y, new_x, 1))
                    visited[new_y][new_x][1] = visited[y][x][visit] + 1
    if visited[n-1][m-1][0] == 0 and visited[n-1][m-1][1] == 0:
        print(-1)
    elif visited[n-1][m-1][0] == 0:
        print(visited[n-1][m-1][1])
    elif visited[n-1][m-1][1] == 0:
        print(visited[n-1][m-1][0])
    else:
        print(min(visited[n-1][m-1][0], visited[n-1][m-1][1]))

search()