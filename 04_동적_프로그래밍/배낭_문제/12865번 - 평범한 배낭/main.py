#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 12865                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: jieunb_b <boj.kr/u/jieunb_b>                +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/12865                          #+#        #+#      #+#     #
#    Solved: 2025/07/04 22:54:28 by jieunb_b      ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
info = [[0, 0]]
for _ in range(n):
    info.append(list(map(int, input().split())))

dp = [[0]*(k+1) for _ in range(n+1)]
for i in range(1, n+1):
    w, v = info[i]
    for j in range(1, k+1):
        if j >= w:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-w]+v)
        else:
            dp[i][j] = dp[i-1][j]
print(dp[-1][-1])

# dp = [0]*(k+1)
# for w, v in info:
#     for i in range(k+1):
#         if i >= w:
#             dp[i] = max(dp[i], dp[i-w]+v)
# print(dp[k])