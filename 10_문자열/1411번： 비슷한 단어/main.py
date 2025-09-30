#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 1411                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: jieunb_b <boj.kr/u/jieunb_b>                +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/1411                           #+#        #+#      #+#     #
#    Solved: 2024/11/13 16:14:17 by jieunb_b      ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

# words_idx = [] # 0120
# for word in words: # word = abca
#     used = [] # 등장한 알파벳 used = abc
#     idx = '' # 바꿀 번호 idx = 0120
#     for i in range(len(word)): # 0 1 2 3
#         if word[i] in used: # word[0] = a
#             idx = idx + str(used.index(word[i]))
#         else:
#             used.append(word[i]) # used = [a]
#             idx = idx + str(len(used)-1)
#     words_idx.append(idx)

import sys
from collections import Counter
input = sys.stdin.readline

N = int(input())

words = []
for _ in range(N):
    word = str(input().strip())
    words.append(word)

words_idx = []
for word in words: 
    used = [] 
    idx = '' 
    for i in range(len(word)):
        if word[i] in used:
            idx = idx + str(used.index(word[i]))
        else:
            used.append(word[i])
            idx = idx + str(len(used)-1)
    words_idx.append(idx)
    
counts = Counter(words_idx)

pair_count = sum((count * (count - 1)) // 2 for count in counts.values())
print(pair_count) 