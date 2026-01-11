#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 14658                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: jieunb_b <boj.kr/u/jieunb_b>                +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/14658                          #+#        #+#      #+#     #
#    Solved: 2025/06/11 20:07:42 by jieunb_b      ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
input = sys.stdin.readline

n, m, l, k = map(int, input().split())
stars = [list(map(int, input().split())) for _ in range(k)]

max_star = 0
for start_x, _ in stars:
    for _, start_y in stars:
        count = 0
        for find_x, find_y in stars:
            if start_x<=find_x<=start_x+l and start_y<=find_y<=start_y+l:
                count += 1 
        max_star = max(max_star, count)
print(k-max_star)