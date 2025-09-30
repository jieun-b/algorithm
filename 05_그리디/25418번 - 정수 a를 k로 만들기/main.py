#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 25418                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: jieunb_b <boj.kr/u/jieunb_b>                +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/25418                          #+#        #+#      #+#     #
#    Solved: 2025/09/23 16:35:04 by jieunb_b      ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
input = sys.stdin.readline

a, k = map(int, input().split())

count = 0
while k > a:
    if k % 2 == 0:
        if k // 2 < a:
            break
        k = k // 2
    else:
        k = k - 1
    count += 1
print(count+k-a)
    
  
