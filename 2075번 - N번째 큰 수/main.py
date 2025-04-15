#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 2075                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: jieunb_b <boj.kr/u/jieunb_b>                +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/2075                           #+#        #+#      #+#     #
#    Solved: 2025/04/16 00:47:57 by jieunb_b      ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
# import sys
# input = sys.stdin.readline

# n = int(input())

# nums = []
# for _ in range(n):
#     inputs = list(map(int, input().split()))
#     for i in inputs:
#         nums.append(i)

# nums = sorted(nums)
# print(nums[-n])

import sys
import heapq
input = sys.stdin.readline

n = int(input())
nums = []
for _ in range(n):
    inputs = list(map(int, input().split()))
    for i in inputs:
        if len(nums) < n:
            heapq.heappush(nums, i)
        else:
            if i > nums[0]:
                heapq.heappushpop(nums, i)

nums = sorted(nums)
print(nums[0])