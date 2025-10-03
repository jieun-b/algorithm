#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 2839                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: jieunb_b <boj.kr/u/jieunb_b>                +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/2839                           #+#        #+#      #+#     #
#    Solved: 2025/10/02 15:32:19 by jieunb_b      ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
input = sys.stdin.readline

n = int(input())
dp = [float('inf')]*(n+1)

if n >= 3:
    dp[3] = 1
if n >= 5:
    dp[5] = 1
if n > 5:
    for i in range(6, n+1):
        dp[i] = min(1+dp[i-3], 1+dp[i-5])

if dp[-1] == float('inf'):
    print(-1)
else:
    print(dp[-1])