#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 1806                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: jieunb_b <boj.kr/u/jieunb_b>                +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/1806                           #+#        #+#      #+#     #
#    Solved: 2025/06/04 16:34:36 by jieunb_b      ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
input = sys.stdin.readline

n, s = map(int, input().split())
a = list(map(int, input().split()))

right = 0
INF = float('inf')
min_sum = INF
current_sum = a[0]
for left in range(n):
    while(current_sum < s and right+1 < n):
        right += 1
        current_sum += a[right]
    if current_sum >= s:
        min_sum = min(min_sum, right-left+1)
    current_sum -= a[left]

if min_sum == INF:
    print(0)
else:
    print(min_sum)