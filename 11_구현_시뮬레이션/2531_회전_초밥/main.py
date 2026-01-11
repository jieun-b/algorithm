#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 2531                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: jieunb_b <boj.kr/u/jieunb_b>                +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/2531                           #+#        #+#      #+#     #
#    Solved: 2025/04/25 16:54:58 by jieunb_b      ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
input = sys.stdin.readline

n, d, k, c = map(int, input().split())
sushi = [int(input()) for _ in range(n)]

max_sushi = 0
for i in range(n):
    if i+k > n:
        unique_sushi = sushi[i:] + sushi[:k-(n-i)]
    else:
        unique_sushi = sushi[i:i+k]
    unique_sushi.append(c)
    unique_sushi = set(unique_sushi)
    max_sushi = max(max_sushi, len(unique_sushi))

print(max_sushi)