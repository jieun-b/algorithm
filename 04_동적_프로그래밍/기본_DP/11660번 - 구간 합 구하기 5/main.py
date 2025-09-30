#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 11660                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: jieunb_b <boj.kr/u/jieunb_b>                +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/11660                          #+#        #+#      #+#     #
#    Solved: 2025/07/04 22:04:20 by jieunb_b      ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
find = [list(map(int, input().split())) for _ in range(m)]

# 전체 구하기
dp = [[0]*n for _ in range(n)]
dp[0][0] = grid[0][0]
for j in range(1, n):
    dp[0][j] = dp[0][j-1] + grid[0][j]
for i in range(1, n):
    dp[i][0] = dp[i-1][0] + grid[i][0]
for i in range(1, n):
    for j in range(1, n):
        dp[i][j] = dp[i][j-1]+dp[i-1][j]-dp[i-1][j-1]+grid[i][j]

# 1,1에서 x2,y2의 합에서 1,1에서 x1,y1의 값 빼기
for x1, y1, x2, y2 in find:
    if x1 != 1 and y1 != 1:
        print(dp[x2-1][y2-1]-(dp[x2-1][y1-2]+dp[x1-2][y2-1])+dp[x1-2][y1-2])
    elif x1 == 1 and y1 == 1:
        print(dp[x2-1][y2-1])
    elif x1 == 1:
        print(dp[x2-1][y2-1]-dp[x2-1][y1-2])
    elif y1 == 1:
        print(dp[x2-1][y2-1]-dp[x1-2][y2-1])