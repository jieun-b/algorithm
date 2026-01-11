#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 2293                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: jieunb_b <boj.kr/u/jieunb_b>                +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/2293                           #+#        #+#      #+#     #
#    Solved: 2025/07/09 23:17:58 by jieunb_b      ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
v = [int(input()) for _ in range(n)]

dp = [0]*(k+1)
for i in range(1, n+1): # 현재 계산할 동전 가치
    value = v[i-1]
    for j in range(1, k+1): # 가치 합
        # 가치 합이 동전 가치보다 작을 경우 -> 그대로
        if j == value:
            dp[j] = dp[j] + 1
        elif j > value:
            dp[j] = dp[j] + dp[j-value]
print(dp[-1])