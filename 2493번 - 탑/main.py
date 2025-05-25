#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 2493                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: jieunb_b <boj.kr/u/jieunb_b>                +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/2493                           #+#        #+#      #+#     #
#    Solved: 2025/05/25 17:50:52 by jieunb_b      ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
input = sys.stdin.readline

n = int(input())
heights = list(map(int, input().split()))

result = [0]*n
stack = []
for i in range(n):
    while(stack and heights[i] > stack[-1][0]):
        stack.pop()
    if stack:
        result[i] = stack[-1][1]
    stack.append((heights[i], i+1))
print(*result)
    


# wall = (0, 0)
# result = [0] * n
# for i in range(1, n):
#     if heights[i] < heights[i-1]:
#         wall = (heights[i-1], i-1+1)
#     result[i] = wall[1]
# print(*result)