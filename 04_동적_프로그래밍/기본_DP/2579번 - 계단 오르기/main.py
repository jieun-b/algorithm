#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 2579                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: jieunb_b <boj.kr/u/jieunb_b>                +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/2579                           #+#        #+#      #+#     #
#    Solved: 2025/10/03 00:07:26 by jieunb_b      ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
input = sys.stdin.readline

n = int(input())
stairs = [int(input()) for _ in range(n)]

if n == 1:
    print(stairs[0])
else:
    dp = [[0]*2 for _ in range(n)]
    dp[0] = [stairs[0], stairs[0]]
    dp[1] = [stairs[1], stairs[0]+stairs[1]]

    if n > 2:
        for i in range(2, n):
            dp[i][0] = dp[i-1][1] + stairs[i]
            dp[i][1] = max(dp[i-2][0], dp[i-2][1]) + stairs[i]
    print(max(dp[-1][0], dp[-1][1]))
