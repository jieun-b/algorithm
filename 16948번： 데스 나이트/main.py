#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 16948                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: jieunb_b <boj.kr/u/jieunb_b>                +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/16948                          #+#        #+#      #+#     #
#    Solved: 2025/03/04 23:53:47 by jieunb_b      ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
r1, c1, r2, c2 = map(int, input().split())

move = [(-2, -1), (-2, 1), (0, -2), (0, 2), (2, -1), (2, 1)]

board = [[0]*n for _ in range(n)]

def bfs(i, j):
    queue = deque([(i, j)])
    while queue:
        r, c = queue.popleft()
        if r == r2 and c == c2:
            print(board[r][c])
            return
        for d in move:
            if 0<=r+d[0]<n and 0<=c+d[1]<n and board[r+d[0]][c+d[1]] == 0:
                board[r+d[0]][c+d[1]] = board[r][c] + 1
                queue.append((r+d[0], c+d[1]))
    print(-1)
    
bfs(r1, c1)