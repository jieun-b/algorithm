#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 1010                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: jieunb_b <boj.kr/u/jieunb_b>                +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/1010                           #+#        #+#      #+#     #
#    Solved: 2025/09/23 16:42:29 by jieunb_b      ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
# import sys
# input = sys.stdin.readline

# t = int(input())
# for _ in range(t):
#     n, m = map(int, input().split())
#     res = 1
#     for i in range(1, n+1):
#         res = res * (m-i+1) // i
#     print(res)

import sys
input = sys.stdin.readline

# 파스칼의 법칙
# 5C2일 때 5를 반드시 포함하는 경우 + 포함하지 않는 경우 = 전체 경우
# 5를 반드시 포함하는 경우: 4C1 -> 5를 제외하고 하나만 고르면 됨
# 5를 포함하지 않는 경우: 4C2 -> 5를 제외하고 2개 골라야 함

#    r=0 1  2   3   4  5
#    n=0 [1, 0, 0, 0, 0, 0]
#    n=1 [1, 1, 0, 0, 0, 0]
#    n=2 [1, 2, 1, 0, 0, 0]
#    n=3 [1, 3, 3, 1, 0, 0]
#    n=4 [1, 4, 6, 4, 1, 0]
#    n=5 [1, 5,10,10, 5, 1]

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    dp = [[0] * (m+1) for _ in range(m+1)]
    for i in range(1, m+1):
        dp[i][0] = 1
        dp[i][i] = 1
        for j in range(1, i):
            dp[i][j] = dp[i-1][j-1]+dp[i-1][j]
    print(dp[m][n])
