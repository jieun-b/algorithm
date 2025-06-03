#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 1253                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: jieunb_b <boj.kr/u/jieunb_b>                +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/1253                           #+#        #+#      #+#     #
#    Solved: 2025/06/03 13:15:19 by jieunb_b      ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
a.sort()

count = 0
for i in range(n):
    left = 0
    right = len(a)-1
    while (left < right):
        if right == i:
            right -= 1
            continue
        elif left == i:
            left += 1
            continue
        if a[i] < a[left] + a[right]:
            right -= 1
        elif a[i] > a[left] + a[right]:
            left += 1
        else:
            count += 1
            break
print(count)