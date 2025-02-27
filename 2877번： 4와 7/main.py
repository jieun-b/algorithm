#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 2877                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: jieunb_b <boj.kr/u/jieunb_b>                +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/2877                           #+#        #+#      #+#     #
#    Solved: 2024/07/02 19:53:43 by jieunb_b      ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
input = sys.stdin.readline
K = int(input())
num = 0
res = 0
while K > 0:
    if K % 2 == 1:
        res += 4*(10 ** num)
    else:
        K = K-1
        res += 7*(10 ** num)
    K = K // 2
    num += 1

print(res)