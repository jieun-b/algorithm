#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 2169                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: jieunb_b <boj.kr/u/jieunb_b>                +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/2169                           #+#        #+#      #+#     #
#    Solved: 2025/06/29 12:06:37 by jieunb_b      ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

INF = -float('inf')

dp = [[INF]*m for _ in range(n)]
# 첫 줄
for j in range(m):
    if j == 0:
        dp[0][j] = graph[0][j]
    else:
        dp[0][j] = dp[0][j-1] + graph[0][j]

for i in range(1, n):
    # 왼쪽
    dp_left = [INF]*m
    for j in range(m):
        if j == 0:
            dp_left[j] = dp[i-1][j] + graph[i][j]
            continue
        dp_left[j] = max(dp[i-1][j] + graph[i][j], dp_left[j-1] + graph[i][j])

    # 오른쪽
    dp_right = [INF]*m
    for j in range(m-1, -1, -1):
        if j == m-1:
            dp_right[j] = dp[i-1][j] + graph[i][j]
            continue
        prev_i, prev_j = i, j+1
        dp_right[j] = max(dp[i-1][j] + graph[i][j], dp_right[j+1] + graph[i][j])

    for j in range(m):
        dp[i][j] = max(dp_left[j], dp_right[j])
print(dp[-1][-1])