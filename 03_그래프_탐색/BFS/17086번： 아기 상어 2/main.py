#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 17086                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: jieunb_b <boj.kr/u/jieunb_b>                +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/17086                          #+#        #+#      #+#     #
#    Solved: 2024/08/15 23:27:41 by jieunb_b      ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
grid = []
for _ in range(N):
    grid.append(list(map(int, input().split())))

direction = ((0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1),(-1,0),(-1,1))

def search(i,j):
    queue = deque()
    visited = [[0]*M for _ in range(N)]
    queue.append((i,j))
    visited[i][j] = 1
    distance = 0
    while(queue):
        current = queue.popleft()
        for d in direction:
            next_i = current[0]+d[0]
            next_j = current[1]+d[1]
            if 0<=next_i<N and 0<=next_j<M and visited[next_i][next_j]==0:
                if grid[next_i][next_j] == 1:
                    distance = visited[current[0]][current[1]]
                else:
                    queue.append((next_i,next_j))
                    visited[next_i][next_j] = visited[current[0]][current[1]]+1
        
        if distance != 0:
            return distance
res = 0 
for i in range(N):
    for j in range(M):
        if grid[i][j] == 0:
            res = max(res,search(i,j))

print(res)