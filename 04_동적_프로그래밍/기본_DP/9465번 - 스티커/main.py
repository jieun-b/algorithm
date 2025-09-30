#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 9465                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: jieunb_b <boj.kr/u/jieunb_b>                +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/9465                           #+#        #+#      #+#     #
#    Solved: 2025/07/05 22:20:12 by jieunb_b      ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
input = sys.stdin.readline   

t = int(input())
for _ in range(t):
    n = int(input())
    dp = [list(map(int, input().split())) for _ in range(2)]
    if n > 1:
        dp[0][1] += dp[1][0]
        dp[1][1] += dp[0][0]
        for i in range(2, n):
            dp[0][i] += max(dp[1][i-1], dp[1][i-2])
            dp[1][i] += max(dp[0][i-1], dp[0][i-2])
        print(max(dp[0][-1], dp[1][-1]))
    else:
        print(*max(dp))