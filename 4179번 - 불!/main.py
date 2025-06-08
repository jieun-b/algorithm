#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 4179                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: jieunb_b <boj.kr/u/jieunb_b>                +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/4179                           #+#        #+#      #+#     #
#    Solved: 2025/06/08 11:22:00 by jieunb_b      ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
from collections import deque
input = sys.stdin.readline

r, c = map(int, input().split())
maze = []
fires = []
for i in range(r):
    row = list(input().strip())
    for j in range(c):
        if row[j] == 'J':
            jihun = (i, j)
        elif row[j] == 'F':
            fires.append((i, j)) 
    maze.append(row)

dx, dy = [1,0,-1,0], [0,1,0,-1]
fire = [[-1]*c for _ in range(r)]
visited = [[-1]*c for _ in range(r)]

def find_fire():
    queue = deque()
    for fy, fx in fires:               
        queue.append((fy, fx))
        fire[fy][fx] = 0
    while(queue):
        y, x = queue.popleft()
        for k in range(4):
            new_y = y + dy[k]
            new_x = x + dx[k]
            if 0<=new_y<r and 0<=new_x<c:
                if maze[new_y][new_x] != '#' and fire[new_y][new_x] == -1:
                    queue.append((new_y, new_x))
                    fire[new_y][new_x] = fire[y][x] + 1

def escape(jihun):
    queue = deque([jihun])
    visited[jihun[0]][jihun[1]] = 0
    while(queue):
        y, x = queue.popleft()
        for k in range(4):
            new_y = y + dy[k]
            new_x = x + dx[k]
            if not (0<=new_y<r and 0<=new_x<c):
                print(visited[y][x] + 1)
                return
            if maze[new_y][new_x] != '#' and visited[new_y][new_x] == -1:
                if fire[new_y][new_x] == -1 or visited[y][x] + 1 < fire[new_y][new_x]:
                    queue.append((new_y, new_x))
                    visited[new_y][new_x] = visited[y][x] + 1
    print('IMPOSSIBLE')

find_fire()
escape(jihun)