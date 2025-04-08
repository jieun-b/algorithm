#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 20920                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: jieunb_b <boj.kr/u/jieunb_b>                +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/20920                          #+#        #+#      #+#     #
#    Solved: 2025/04/07 14:23:02 by jieunb_b      ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
from collections import Counter
input = sys.stdin.readline

n, m = map(int, input().split())
words = []
for _ in range(n):
    word = input().strip()
    if len(word) >= m:
        words.append(word)

words_count = Counter(words)
words_count = sorted(words_count.items(), key=lambda x: (-x[1], -len(x[0]), x[0]))

for word, num in words_count:
    print(word)

# 자주 나오는 단어 -> counters로 개수 세기 
    # 단어의 길이
        # 알파벳 사전 순
