#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 9251                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: jieunb_b <boj.kr/u/jieunb_b>                +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/9251                           #+#        #+#      #+#     #
#    Solved: 2025/07/09 21:09:33 by jieunb_b      ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
input = sys.stdin.readline

a = ' '+input().strip()
b = ' '+input().strip()

dp = [[0]*len(a) for _ in range(len(b))]
# b\a A C A Y K P
#   C 0 1 1 1 1 1
#   A 1 1 2 2 2 2
#   P 1 1 2 2 2 3
#   C 1 2 2 2 2 3
#   A 2 2 3 3 3 3
#   K 2 2 3 3 4 4

for i in range(1, len(b)):
    for j in range(1, len(a)):
        if b[i] == a[j]:
            # 같을 때 -> 큰거 + 1
            # 이전 단어들이 서로 다르거나 완전
            # 이전 단어랑도 같을 경우 b[i-1], a[j-1]이랑 같아야 만족 아니면 패스 
      
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            # 다를 때 -> 위가 있으면 그대로 내려오기, 위나 왼쪽 중 큰거
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

print(max(dp[-1]))