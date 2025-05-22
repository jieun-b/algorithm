#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 1522                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: jieunb_b <boj.kr/u/jieunb_b>                +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/1522                           #+#        #+#      #+#     #
#    Solved: 2025/05/22 11:18:46 by jieunb_b      ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
input = sys.stdin.readline

arr = list(input().strip())
size = arr.count('a')

min_count = size
for i in range(len(arr)):
    if i+size > len(arr):
        window = arr[i:]+arr[:size-(len(arr)-i)]
    else:
        window = arr[i:i+size]
    count = window.count('b')
    min_count = min(count, min_count)
print(min_count)