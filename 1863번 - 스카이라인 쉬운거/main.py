#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 1863                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: jieunb_b <boj.kr/u/jieunb_b>                +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/1863                           #+#        #+#      #+#     #
#    Solved: 2025/05/31 23:14:14 by jieunb_b      ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
input = sys.stdin.readline

n = int(input())
stack = []
count = 0
for _ in range(n):
    x, y = map(int, input().split())
    while stack and stack[-1] > y:
        stack.pop()
        count += 1
    if not stack or stack[-1] < y:
        if y != 0:
            stack.append(y)
  
print(count+len(stack))