#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 11501                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: jieunb_b <boj.kr/u/jieunb_b>                +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/11501                          #+#        #+#      #+#     #
#    Solved: 2025/04/14 17:45:33 by jieunb_b      ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    values = list(map(int, input().split()))

    max_profit = 0
    max_value = 0
    for i in range(len(values)-1, -1, -1):
        if max_value < values[i]:
            max_value = values[i]
        else:
            max_profit += max_value - values[i]
    print(max_profit)