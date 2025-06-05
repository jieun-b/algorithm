#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 2110                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: jieunb_b <boj.kr/u/jieunb_b>                +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/2110                           #+#        #+#      #+#     #
#    Solved: 2025/06/04 19:31:32 by jieunb_b      ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
input = sys.stdin.readline

n, c = map(int, input().split())
x = [int(input()) for _ in range(n)]
x.sort()

left = 1
right = x[-1] - x[0]
result = 0

while left <= right:
    mid = (left + right) // 2

    count = 1
    last = x[0]
    for i in range(1, n):
        if x[i] - last >= mid:
            count += 1
            last = x[i]

    if count >= c:
        result = mid 
        left = mid + 1
    else:
        right = mid - 1

print(result)