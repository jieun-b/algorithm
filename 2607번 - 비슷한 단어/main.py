#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 2607                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: jieunb_b <boj.kr/u/jieunb_b>                +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/2607                           #+#        #+#      #+#     #
#    Solved: 2025/04/11 02:39:42 by jieunb_b      ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
from collections import Counter
input = sys.stdin.readline

n = int(input())
word = input().strip()
words = [input().strip() for _ in range(n-1)]

word_counter = Counter(word)

count = 0
for w in words:
    if len(word) >= len(w):
        if sum((word_counter-Counter(w)).values()) <= 1:
            count += 1
    else:
        if sum((Counter(w)-word_counter).values()) == 1:
            count += 1
print(count)