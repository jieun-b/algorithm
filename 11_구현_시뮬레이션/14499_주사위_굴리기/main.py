#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 14499                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: jieunb_b <boj.kr/u/jieunb_b>                +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/14499                          #+#        #+#      #+#     #
#    Solved: 2026/01/14 23:19:40 by jieunb_b      ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
input = sys.stdin.readline

n, m, x, y, k = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
order = list(map(int, input().split()))

dice = [0, 0, 0, 0, 0, 0] # 위 아래 북 남 동 서
rot = {
    1: [5, 4, 2, 3, 0, 1], # 동
    2: [4, 5, 2, 3, 1, 0], # 서
    3: [3, 2, 0, 1, 4, 5], # 북
    4: [2, 3, 1, 0, 4, 5], # 남
}

dx = [0, 0, -1, 1] # 동 서 북 남
dy = [1, -1, 0, 0]

for dir in order:
    nx, ny = x+dx[dir-1], y+dy[dir-1]
    if 0<=nx<n and 0<=ny<m:
        x, y = nx, ny
        dice = [dice[idx] for idx in rot[dir]]
        if graph[x][y] == 0:
            graph[x][y] = dice[1]
        else:
            dice[1] = graph[x][y]
            graph[x][y] = 0
        print(dice[0])