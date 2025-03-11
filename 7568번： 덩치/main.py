#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 7568                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: jieunb_b <boj.kr/u/jieunb_b>                +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/7568                           #+#        #+#      #+#     #
#    Solved: 2025/03/11 15:11:54 by jieunb_b      ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
input = sys.stdin.readline

n = int(input())
info = [list(map(int, input().split())) for _ in range(n)]

ranks = []
for i in range(n):
    rank = 1
    for j in range(n): # 자기보다 덩치 큰 사람 수 세기
        if i != j and info[i][0] < info[j][0] and info[i][1] < info[j][1]:
            rank += 1
    ranks.append(rank)

print(*ranks)