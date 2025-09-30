#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 1213                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: jieunb_b <boj.kr/u/jieunb_b>                +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/1213                           #+#        #+#      #+#     #
#    Solved: 2025/09/23 16:12:36 by jieunb_b      ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
# import sys
# from collections import defaultdict
# input = sys.stdin.readline

# name = input().strip()

# alphabets = defaultdict(int)
# for alphabet in name:
#     alphabets[alphabet] += 1

# middle = ''
# middle_cnt = 0
# for alphabet in alphabets:
#     if alphabets[alphabet] % 2 != 0:
#         middle = alphabet
#         middle_cnt += 1

# if middle_cnt > 1:
#     print("I'm Sorry Hansoo")
#     exit()

# words = []
# for alphabet in alphabets:
#     words.append((alphabets[alphabet] // 2) * alphabet)

# print("".join(sorted(words))+middle+"".join(sorted(words, reverse=True)))


import sys
from collections import Counter
input = sys.stdin.readline

count = Counter(input().strip())

words = []
middle = ''
for c in count:
    if count[c] % 2 == 1:
        if middle != '':
            print("I'm Sorry Hansoo")
            exit()
        middle = c
    words.append(c*(count[c] // 2))

print("".join(sorted(words))+middle+"".join(sorted(words, reverse=True)))