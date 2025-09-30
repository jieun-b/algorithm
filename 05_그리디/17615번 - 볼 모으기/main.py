#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 17615                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: jieunb_b <boj.kr/u/jieunb_b>                +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/17615                          #+#        #+#      #+#     #
#    Solved: 2025/04/24 23:07:25 by jieunb_b      ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
from collections import Counter
input = sys.stdin.readline

n = int(input())
colors = list(input().strip())
color_count = Counter(colors)

# 각 양 끝에 무더기가 몇개 있는지 확인만 하면 됨
count = 0
for color in colors:
    if color == 'R':
        count += 1
    else:
        break
result = color_count['R'] - count

count = 0
for color in reversed(colors):
    if color == 'R':
        count += 1
    else:
        break
result = min(result, color_count['R'] - count)

count = 0
for color in colors:
    if color == 'B':
        count += 1
    else:
        break
result = min(result, color_count['B'] - count)

count = 0
for color in reversed(colors):
    if color == 'B':
        count += 1
    else:
        break
result = min(result, color_count['B'] - count)
print(result)