#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 2565                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: jieunb_b <boj.kr/u/jieunb_b>                +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/2565                           #+#        #+#      #+#     #
#    Solved: 2025/07/10 21:54:56 by jieunb_b      ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
input = sys.stdin.readline

n = int(input())
pos = [list(map(int, input().split())) for _ in range(n)]
pos.sort()

# 각 전기줄의 위치에서 교차 없이 가질 수 있는 전기줄의 수
dp = [1]*n 
for i in range(1, n):
    for j in range(i):
        if pos[i][1] > pos[j][1]:
            dp[i] = max(dp[i], dp[j]+1)
print(n-max(dp))