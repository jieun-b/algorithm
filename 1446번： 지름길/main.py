#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 1446                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: jieunb_b <boj.kr/u/jieunb_b>                +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/1446                           #+#        #+#      #+#     #
#    Solved: 2024/09/18 19:16:58 by jieunb_b      ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

import sys
input = sys.stdin.readline

N, D = map(int, input().split())

short = []
for _ in range(N):
    info = list(map(int, input().split()))
    short.append(info)

road = [i for i in range(D+1)]

for i in range(D+1):
    road[i] = min(road[i], road[i-1]+1)
    for start, end, length in short:
        if start == i and end <= D and road[end] > road[i]+length:
            road[end] = road[i]+length 

print(road[D])