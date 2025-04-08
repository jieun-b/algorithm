#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 13305                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: jieunb_b <boj.kr/u/jieunb_b>                +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/13305                          #+#        #+#      #+#     #
#    Solved: 2025/04/07 13:46:58 by jieunb_b      ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
input = sys.stdin.readline

n = int(input())
road = list(map(int, input().split()))
price = list(map(int, input().split()))

min_price = 1000000000
min_idx = 0

price_sum = 0

for i in range(n-1):
    min_price = min(min_price, price[i])
    price_sum += min_price * road[i]

print(price_sum)