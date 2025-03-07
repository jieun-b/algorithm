#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 5073                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: jieunb_b <boj.kr/u/jieunb_b>                +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/5073                           #+#        #+#      #+#     #
#    Solved: 2025/03/07 22:27:08 by jieunb_b      ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
input = sys.stdin.readline

while True:
    triangle = list(map(int, input().split()))
    if all(side == 0 for side in triangle):
        exit()
    triangle.sort(reverse=True)
    if triangle[0] == triangle[1] == triangle[2]:
        print('Equilateral')
    elif triangle[0] >= triangle[1] + triangle[2]:
        print('Invalid')
    elif triangle[0] == triangle[1] or triangle[1] == triangle[2]:
        print('Isosceles')
    else:
        print('Scalene')