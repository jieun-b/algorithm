#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 16234                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: jieunb_b <boj.kr/u/jieunb_b>                +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/16234                          #+#        #+#      #+#     #
#    Solved: 2025/05/29 21:30:52 by jieunb_b      ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
from collections import deque
input = sys.stdin.readline

n, l, r = map(int, input().split())
countries = [list(map(int, input().split())) for _ in range(n)]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def search(i, j):
    queue = deque([(i,j)])
    visited[i][j] = True
    union = [countries[i][j], (i, j)]
    while(queue):
        y, x = queue.popleft()
        for k in range(4):
            new_y = y + dy[k]
            new_x = x + dx[k]
            if 0<=new_y<n and 0<=new_x<n and not visited[new_y][new_x]:
                if l<=abs(countries[y][x] - countries[new_y][new_x])<=r:
                    queue.append((new_y, new_x))
                    visited[new_y][new_x] = True
                    union.append((new_y, new_x))
                    union[0] += countries[new_y][new_x]
    if union == [countries[i][j], (i, j)]:
        return []
    return union

count = 0
while(True):
    visited = [[False]*n for _ in range(n)]
    info = []
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                union = search(i, j) 
                if union:
                    info.append(union) 
    if not info:
        break
    else:
        for union in info:
            population = union[0] // (len(union)-1)
            for i in range(1, len(union)):
                countries[union[i][0]][union[i][1]] = population
        count += 1
print(count)