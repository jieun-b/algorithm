#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 9084                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: jieunb_b <boj.kr/u/jieunb_b>                +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/9084                           #+#        #+#      #+#     #
#    Solved: 2025/07/22 22:52:43 by jieunb_b      ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    coins = map(int, input().split())
    m = int(input())

    # 모든 금액을 만드는 경우의 수 구하기
    dp = [0]*(m+1)
    dp[0] = 1
    for coin in coins:
        for i in range(coin, m+1):
            dp[i] += dp[i-coin]
    print(dp[-1])