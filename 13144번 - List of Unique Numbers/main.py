#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 13144                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: jieunb_b <boj.kr/u/jieunb_b>                +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/13144                          #+#        #+#      #+#     #
#    Solved: 2025/06/05 12:13:06 by jieunb_b      ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

left, right = 0, 0
count = 0
check = set()
while(left<=right and left < n):
    if right < n and arr[right] not in check:
        check.add(arr[right])
        right += 1
    else:
        count += right-left
        check.remove(arr[left])
        left += 1

print(count) 
