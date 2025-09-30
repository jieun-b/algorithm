#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 11758                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: jieunb_b <boj.kr/u/jieunb_b>                +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/11758                          #+#        #+#      #+#     #
#    Solved: 2025/07/31 21:25:20 by jieunb_b      ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
input = sys.stdin.readline

p1 = list(map(int, input().split()))
p2 = list(map(int, input().split()))
p3 = list(map(int, input().split()))

p1p2 = (p2[0]-p1[0], p2[1]-p1[1])
p2p3 = (p3[0]-p2[0], p3[1]-p2[1])

d = p1p2[0]*p2p3[1]-p1p2[1]*p2p3[0]
if d > 0:
    print(1)
elif d < 0:
    print(-1)
else:
    print(0)