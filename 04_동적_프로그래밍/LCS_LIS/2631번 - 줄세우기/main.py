#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 2631                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: jieunb_b <boj.kr/u/jieunb_b>                +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/2631                           #+#        #+#      #+#     #
#    Solved: 2025/06/07 14:57:16 by jieunb_b      ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
input = sys.stdin.readline

n = int(input())
num = [int(input()) for _ in range(n)]
dp = [1 for _ in range(n)]

for i in range(n):
    for j in range(i):
        if num[i] > num[j]:
            dp[i] = max(dp[i], dp[j]+1)

print(n - max(dp))