#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 2467                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: jieunb_b <boj.kr/u/jieunb_b>                +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/2467                           #+#        #+#      #+#     #
#    Solved: 2025/05/26 21:59:45 by jieunb_b      ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
input = sys.stdin.readline

n = int(input())
att = list(map(int, input().split()))

left = 0
right = len(att)-1
min_result = float('inf')
while(left < right):
    if abs(att[left]+att[right]) < min_result:
        min_result = abs(att[right]+att[left])
        result = [att[left], att[right]]
    if abs(att[left+1]+att[right]) < abs(att[left]+att[right-1]):
        left += 1
    else: 
        right -= 1

print(*result)