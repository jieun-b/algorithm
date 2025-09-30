#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 1157                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: jieunb_b <boj.kr/u/jieunb_b>                +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/1157                           #+#        #+#      #+#     #
#    Solved: 2025/03/08 15:16:42 by jieunb_b      ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
input = sys.stdin.readline

word = input().strip()
word = word.upper()

alphabet = dict()
for char in word:
    if not char in alphabet:
        alphabet[char] = 1
    else:
        alphabet[char] += 1

alphabet = sorted(alphabet.items(), key=lambda x:x[1], reverse=True)
if len(alphabet) > 1 and alphabet[0][1] == alphabet[1][1]:
    print('?')
else:
    print(alphabet[0][0])