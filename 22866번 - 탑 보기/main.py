#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 22866                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: jieunb_b <boj.kr/u/jieunb_b>                +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/22866                          #+#        #+#      #+#     #
#    Solved: 2025/06/14 00:15:38 by jieunb_b      ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
input = sys.stdin.readline

n = int(input())
heights = list(map(int, input().split()))

count = [0]*n

left_stack = []
left = [-1]*n
for i in range(n):
    while(left_stack and left_stack[-1][1] <= heights[i]):
        left_stack.pop()
    count[i] = len(left_stack)
    if left_stack:
        left[i] = left_stack[-1][0]
    left_stack.append((i, heights[i]))

right_stack = []
right = [-1]*n
for i in range(n-1, -1, -1):
    while(right_stack and right_stack[-1][1] <= heights[i]):
        right_stack.pop()
    count[i] += len(right_stack)
    if right_stack:
        right[i] = right_stack[-1][0]
    right_stack.append((i, heights[i]))

for i in range(n):
    if left[i] == -1 and right[i] == -1:
        print(0)
        continue
    if left[i] == -1 or abs(i-left[i]) > abs(i-right[i]):
        num = right[i]+1
    elif right[i] == -1 or abs(i-left[i]) <= abs(i-right[i]):
        num = left[i]+1
    print(count[i], num)