#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 1027                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: jieunb_b <boj.kr/u/jieunb_b>                +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/1027                           #+#        #+#      #+#     #
#    Solved: 2025/06/06 14:14:18 by jieunb_b      ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
input = sys.stdin.readline

n = int(input())
heights = list(map(int, input().split()))

max_building = 0
for i in range(n):
    count = 0
    left, right = float('-inf'), float('-inf')
    # right
    for j in range(i+1, n):
        slope = (heights[j]-heights[i])/(j-i)
        if slope > right:
            count += 1
            right = max((heights[j]-heights[i])/(j-i), right)
        
    # left
    for j in range(i-1, -1, -1):
        slope = (heights[j]-heights[i])/(i-j)
        if slope > left:
            count += 1
            left = max((heights[j]-heights[i])/(i-j), left)
        
    max_building = max(max_building, count)
print(max_building)