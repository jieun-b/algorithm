#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 13460                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: jieunb_b <boj.kr/u/jieunb_b>                +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/13460                          #+#        #+#      #+#     #
#    Solved: 2025/03/05 13:35:00 by jieunb_b      ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
from collections import deque
input = sys.stdin.readline
 
n, m = map(int, input().split())
board = [list(input().strip()) for _ in range(n)]
visited = [[[[0]*m for _ in range(n)] for _ in range(m)] for _ in range(n)]

dy = [0,1,0,-1]
dx = [1,0,-1,0]

for i in range(n):
    for j in range(m):
        if board[i][j] == "#":
            visited[i][j][i][j] = 1
        if board[i][j] == "R":
            ry, rx = i, j
        if board[i][j] == "B":
            by, bx = i, j

def move(y, x, dy, dx): # 현재 위치, 방향
    count = 0
    while board[y+dy][x+dx] != '#' and board[y][x] != 'O':
        y += dy
        x += dx
        count += 1
    return y, x, count

def search(r_y, r_x, b_y, b_x):
    queue = deque([(r_y, r_x, b_y, b_x, 1)])
    visited[r_y][r_x][b_y][b_x] = 1
    while queue:
        ry, rx, by, bx, depth = queue.popleft()
        if depth > 10:
            break
        for k in range(4):
            new_ry, new_rx, count_r = move(ry, rx, dy[k], dx[k])
            new_by, new_bx, count_b = move(by, bx, dy[k], dx[k])
            if board[new_by][new_bx] == 'O':
                continue
            if board[new_ry][new_rx] == 'O':
                return depth
            if new_ry == new_by and new_rx == new_bx:
                if count_r > count_b:
                    new_ry, new_rx = new_ry-dy[k], new_rx-dx[k]
                else: 
                    new_by, new_bx = new_by-dy[k], new_bx-dx[k]
            if visited[new_ry][new_rx][new_by][new_bx] == 0:
                visited[new_ry][new_rx][new_by][new_bx] = 1
                queue.append((new_ry, new_rx, new_by, new_bx, depth+1))
    return -1

print(search(ry, rx, by, bx))

# def search(trying, ry, rx, by, bx, dir): # 시도 횟수, 빨간 구슬 위치, 파란 구슬 위치
#     global min_trying
#     # 만약 시도가 10보다 크면 종
#     if trying > 10:
#         return
#     if by == oy and bx == ox:
#         return
#     if ry == oy and rx == ox:
#         min_trying = min(min_trying, trying)
#     for k in range(4):
#         new_ry, new_rx = ry+dy[k], rx+dx[k]
#         new_by, new_bx = by+dy[k], bx+dx[k]

#         if visited_r[new_ry][new_rx] and visited_b[new_by][new_bx]: 
#             continue
#         if not visited_r[new_ry][new_rx] and visited_b[new_by][new_bx]: 
#             new_by, new_bx = by, bx
#         if visited_r[new_ry][new_rx] and not visited_b[new_by][new_bx]:
#             new_ry, new_rx = ry, rx
#         if new_ry == new_by and new_rx == new_bx:
#             continue
        
#         if dir != k:
#             new_trying = trying + 1
#         else:
#             new_trying = trying
#         visited_r[new_ry][new_rx] = visited_b[new_by][new_bx] = 1
#         search(new_trying, new_ry, new_rx, new_by, new_bx, k)
#         visited_r[new_ry][new_rx] = visited_b[new_by][new_bx] = 0

# min_trying = 11
# visited_r[ry][rx] = visited_b[by][bx] = 1
# search(0, ry, rx, by, bx, -1)
# if min_trying == 11:
#     print(-1)
# else:
#     print(min_trying)