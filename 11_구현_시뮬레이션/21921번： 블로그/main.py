#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 21921                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: jieunb_b <boj.kr/u/jieunb_b>                +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/21921                          #+#        #+#      #+#     #
#    Solved: 2025/04/08 17:58:20 by jieunb_b      ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
input = sys.stdin.readline

n, x = map(int, input().split())
todays = list(map(int, input().split()))

today = sum(todays[:x])
today_max = today
today_max_count = 1

for i in range(1, n-x+1):
    today = today + todays[i+x-1] - todays[i-1]
    if today > today_max:
        today_max = today
        today_max_count = 1
    elif today == today_max:
        today_max_count += 1
        
if today_max == 0:
    print('SAD')
else:
    print(today_max)
    print(today_max_count)