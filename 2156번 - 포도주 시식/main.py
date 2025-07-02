#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 2156                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: jieunb_b <boj.kr/u/jieunb_b>                +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/2156                           #+#        #+#      #+#     #
#    Solved: 2025/07/02 18:06:16 by jieunb_b      ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
input = sys.stdin.readline

n = int(input())
info = [int(input()) for _ in range(n)]

INF = float('inf')
dp = [INF]*n
dp[0] = info[0]

if n > 1:
    dp[1] = info[1]+dp[0]
if n > 2:
    dp[2] = max(dp[1], info[1]+info[2], info[0]+info[2])

for i in range(3, n):
    dp[i] = max(dp[i-1], dp[i-3]+info[i-1]+info[i], dp[i-2]+info[i])
print(dp[-1])

# dp = [[INF]*3 for _ in range(n)]

# for i in range(3):
#     dp[0][i] = info[0]
# for i in range(1, n):
#     if i == 1:
#         dp[i][0] = info[i]
#         dp[i][1] = dp[i-1][1]
#         dp[i][2] = info[i]+dp[i-1][2]
#         continue
#     if i % 3 == 0:
#         dp[i][0] = dp[i-1][0]
#         dp[i][1] = info[i]+dp[i-1][1]
#         dp[i][2] = info[i]+dp[i-2][2]
#     elif i % 3 == 1:
#         dp[i][0] = info[i]+dp[i-2][0]
#         dp[i][1] = dp[i-1][1]
#         dp[i][2] = info[i]+dp[i-1][2]
#     else:
#         dp[i][0] = info[i]+dp[i-1][0]
#         dp[i][1] = info[i]+dp[i-2][1]
#         dp[i][2] = dp[i-1][2]
# print(dp)
# print(max(dp[-1]))