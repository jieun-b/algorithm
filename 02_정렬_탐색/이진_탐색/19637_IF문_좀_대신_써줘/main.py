#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 19637                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: jieunb_b <boj.kr/u/jieunb_b>                +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/19637                          #+#        #+#      #+#     #
#    Solved: 2025/04/12 16:43:49 by jieunb_b      ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
info = []
for _ in range(n):
    name, power = input().split()
    info.append([name, int(power)])

for _ in range(m):
    character = int(input())
    left, right = 0, len(info)
    while left < right:
        mid = (left + right) // 2
        if info[mid][1] < character:
            left = mid + 1
        else:
            right = mid
    print(info[left][0])