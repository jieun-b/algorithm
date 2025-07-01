#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 1932                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: jieunb_b <boj.kr/u/jieunb_b>                +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/1932                           #+#        #+#      #+#     #
#    Solved: 2025/07/02 00:14:03 by jieunb_b      ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
input = sys.stdin.readline

n = int(input())

INF = float('inf')
triangle = [list(map(int, input().split())) for _ in range(n)]
dp = [[INF]*(i+1) for i in range(n)]

for i in range(n):
    if i == 0:
        dp[i][i] = triangle[i][i]
        continue
    for j in range(i+1):
        if j-1<0:
            dp[i][j] = triangle[i][j] + dp[i-1][j]
        elif j>=i:
            dp[i][j] = triangle[i][j] + dp[i-1][j-1]
        else:
            dp[i][j] = max(triangle[i][j] + dp[i-1][j-1], triangle[i][j] + dp[i-1][j])

print(max(dp[-1]))