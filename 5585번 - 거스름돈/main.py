#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 5585                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: jieunb_b <boj.kr/u/jieunb_b>                +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/5585                           #+#        #+#      #+#     #
#    Solved: 2025/07/28 23:11:13 by jieunb_b      ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
input = sys.stdin.readline

n = int(input())

money = [500, 100, 50, 10, 5, 1]
res = 0
n = 1000-n
for i in range(len(money)):
    res += n // money[i]
    n = n % money[i]
    
print(res)