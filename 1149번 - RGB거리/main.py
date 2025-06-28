#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 1149                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: jieunb_b <boj.kr/u/jieunb_b>                +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/1149                           #+#        #+#      #+#     #
#    Solved: 2025/06/28 13:43:12 by jieunb_b      ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
input = sys.stdin.readline

n = int(input())
costs = [list(map(int, input().split())) for _ in range(n)]

dp = [[0]*3 for _ in range(n)]
for k in range(3):
    dp[0][k] = costs[0][k]

for i in range(1, n):
    dp[i][0] = min(dp[i-1][1]+costs[i][0], dp[i-1][2]+costs[i][0])
    dp[i][1] = min(dp[i-1][0]+costs[i][1], dp[i-1][2]+costs[i][1])
    dp[i][2] = min(dp[i-1][0]+costs[i][2], dp[i-1][1]+costs[i][2])
print(min(dp[-1]))