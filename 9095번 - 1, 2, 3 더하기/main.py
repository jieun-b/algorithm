#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 9095                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: jieunb_b <boj.kr/u/jieunb_b>                +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/9095                           #+#        #+#      #+#     #
#    Solved: 2025/09/15 13:03:15 by jieunb_b      ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    if n == 1:
        print(1)
    elif n == 2:
        print(2)
    elif n == 3:
        print(4)
    else:
        dp = [0] * (n+1)
        dp[1] = 1
        dp[2] = 2
        dp[3] = 4
        for i in range(4, len(dp)):
            dp[i] = dp[i-1]+dp[i-2]+dp[i-3]
        print(dp[-1])