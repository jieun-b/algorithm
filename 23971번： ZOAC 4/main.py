#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 23971                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: jieunb_b <boj.kr/u/jieunb_b>                +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/23971                          #+#        #+#      #+#     #
#    Solved: 2025/03/07 22:15:00 by jieunb_b      ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
input = sys.stdin.readline

h, w, n, m = map(int, input().split())

height = h//(n+1)
if h%(n+1) != 0:
    height += 1

width = w//(m+1)
if w%(m+1) != 0:
    width += 1

print(height*width)