#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 2636                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: jieunb_b <boj.kr/u/jieunb_b>                +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/2636                           #+#        #+#      #+#     #
#    Solved: 2024/06/25 23:54:56 by jieunb_b      ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
from collections import deque
from copy import deepcopy
input = sys.stdin.readline

def exclude(i,j):
    queue = deque()
    check[i][j] = 0
    queue.append((i,j))
    while(queue):
        y, x = queue.popleft()
        for k in range(4):
            ny = y + dy[k]
            nx = x + dx[k]
            if 0<=ny<h and 0<=nx<w:
                if check[ny][nx] == 1 and grid[ny][nx] == 0:
                    check[ny][nx] = 0
                    queue.append((ny,nx))

def search(i,j):
    flag = False
    for k in range(4):
        ny = i + dy[k]
        nx = j + dx[k]
        if 0<=ny<h and 0<=nx<w and check[ny][nx] == 0:
            flag = True
    if flag:
        new[i][j] = 0

h, w = map(int, input().split())
grid = []
for _ in range(h):
    row = list(map(int, input().split()))
    grid.append(row)

dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

hour = 0
cheese = 0
while(True):
    hour += 1
    check = [[1]*w for _ in range(h)]
    exclude(0,0)
    new = deepcopy(check)
    for i in range(h):
        for j in range(w):
            if check[i][j] == 1:
                if grid[i][j] == check[i][j]:
                    search(i,j)
                else:
                    new[i][j] = 0
    grid = deepcopy(new)
    num = 0
    for i in range(h):
        for j in range(w):
            if grid[i][j] == 1:
                num += 1
    if num == 0:
        break
    cheese = num

print(hour)
print(cheese)