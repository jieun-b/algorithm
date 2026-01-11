#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 2018                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: jieunb_b <boj.kr/u/jieunb_b>                +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/2018                           #+#        #+#      #+#     #
#    Solved: 2025/10/11 23:49:53 by jieunb_b      ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
input = sys.stdin.readline

n = int(input())

left, right = 1, 1
total = 1
res = 0
while left <= right:
    # 합이 작으면 right 늘리기
    # 조건 채우면 left 늘리기 혹은 합이 커지면 left 늘리기
    if total == n:
        res += 1
        if right == n:
            break
    if total > n:    
        total -= left 
        left += 1
    else:
        right += 1
        total += right  
print(res)