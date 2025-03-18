#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 1205                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: jieunb_b <boj.kr/u/jieunb_b>                +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/1205                           #+#        #+#      #+#     #
#    Solved: 2025/03/18 21:49:18 by jieunb_b      ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
input = sys.stdin.readline

n, score, p = map(int, input().split())
if n == 0:
    print(1)
else:
    ranks = list(map(int, input().split()))
    # n이 p랑 같을 때 맨 끝에 있는거보다 점수가 낮으면 print -1
    if n == p and ranks[-1] >= score:
        print(-1)
    else:
        rank = n+1
        for i in range(len(ranks)):
            if ranks[i] <= score:
                rank = i+1
                break
        print(rank)
            