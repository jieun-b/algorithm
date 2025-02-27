#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 14502                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: jieunb_b <boj.kr/u/jieunb_b>                +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/14502                          #+#        #+#      #+#     #
#    Solved: 2024/06/26 02:07:17 by jieunb_b      ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
from collections import deque
from copy import deepcopy
input = sys.stdin.readline
N, M = map(int, input().split())
grid = []
for _ in range(N):
    grid.append(list(map(int, input().split())))

dy = [0,1,0,-1]
dx = [1,0,-1,0]

def search(i,j,tmp):
    queue = deque()
    queue.append((i,j))
    while(queue):
        y,x = queue.popleft()
        for k in range(4):
            ny = y + dy[k]
            nx = x + dx[k]
            if 0<=ny<N and 0<=nx<M and tmp[ny][nx] == 0:
                tmp[ny][nx] = 2
                queue.append((ny,nx))

def build(cnt):
    global res
    if cnt == 3:
        tmp = deepcopy(grid)
        for a in range(N):
            for b in range(M):
                if tmp[a][b] == 2:
                    search(a,b,tmp)
        count = 0
        for a in range(N):
            for b in range(M):
                if tmp[a][b] == 0:
                    count += 1
        res = max(count, res)
        return
    for i in range(N):
        for j in range(M):
            if grid[i][j] == 0:
                grid[i][j] = 1
                build(cnt+1)
                grid[i][j] = 0

res = 0
build(0)
print(res)