#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 5073                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: jieunb_b <boj.kr/u/jieunb_b>                +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/5073                           #+#        #+#      #+#     #
#    Solved: 2025/09/04 13:52:01 by jieunb_b      ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
input = sys.stdin.readline

while(True):
    edge = list(map(int, input().split()))
    if edge == [0, 0, 0]:
        break
    edge.sort()
    if edge[0] == edge[1] and edge[1] == edge[2]:
        print('Equilateral')
    elif edge[2] < edge[0] + edge[1]:
        if edge[0] == edge[1] or edge[1] == edge[2]:  
            print('Isosceles')
        else:
            print('Scalene')
    else:
        print('Invalid')