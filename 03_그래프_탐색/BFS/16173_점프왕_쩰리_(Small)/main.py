#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 16173                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: jieunb_b <boj.kr/u/jieunb_b>                +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/16173                          #+#        #+#      #+#     #
#    Solved: 2025/09/11 14:34:59 by jieunb_b      ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]

# 최단 거리 문제는 아님
# 조건에 만족해서 게임에서 이길 수 있는지만 판단하면 됨
# 모든 구역을 다 가봐야 함
# 2<=n<=3으로 입력 제한이 매우 작음
# n이 3일 때 오른쪽과 아래쪽을 고려 -> 방향 고려는 제곱승

d = [[0, 1], [1, 0]]

def search(i, j):
    queue = deque([(i, j)])
    visited[i][j] = True
    while(queue):
        i, j = queue.popleft()
        if board[i][j] == -1:
            return "HaruHaru"
        for k in range(2):
            new_i, new_j = i + d[k][0]*board[i][j], j + d[k][1]*board[i][j]
            if 0<=new_i<n and 0<=new_j<n and not visited[new_i][new_j]:
                queue.append((new_i, new_j))
                visited[new_i][new_j] = True
    return "Hing"

visited = [[False]*n for _ in range(n)]
print(search(0, 0))