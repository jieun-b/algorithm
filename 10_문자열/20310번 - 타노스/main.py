#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 20310                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: jieunb_b <boj.kr/u/jieunb_b>                +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/20310                          #+#        #+#      #+#     #
#    Solved: 2025/04/11 19:18:16 by jieunb_b      ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
from collections import Counter
input = sys.stdin.readline

s = list(input().strip())
counter = Counter(s)

zero = counter['0']//2
one = counter['1']//2

for _ in range(one):
    s.pop(s.index('1'))
for _ in range(zero):
    s.pop(-s[::-1].index('0')-1)

print(''.join(s))