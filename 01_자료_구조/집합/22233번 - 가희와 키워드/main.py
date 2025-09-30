#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 22233                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: jieunb_b <boj.kr/u/jieunb_b>                +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/22233                          #+#        #+#      #+#     #
#    Solved: 2025/04/13 16:15:24 by jieunb_b      ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
keywords = dict()
for _ in range(n):
    keywords[input().strip()] = 1

count = n
for _ in range(m):
    written = input().strip().split(',')
    for word in written:
        if word in keywords.keys():
            if keywords[word] == 1:
                keywords[word] -= 1
                count -= 1
    print(count)