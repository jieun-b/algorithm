#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 1476                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: jieunb_b <boj.kr/u/jieunb_b>                +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/1476                           #+#        #+#      #+#     #
#    Solved: 2025/09/11 14:01:16 by jieunb_b      ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
input = sys.stdin.readline

e, s, m = map(int, input().split())
cnt = [0, 0, 0]
total = 0
while [e, s, m] != cnt:
    total += 1
    cnt[0] += 1
    cnt[1] += 1
    cnt[2] += 1
    if cnt[0] > 15:
        cnt[0] = 1
    if cnt[1] > 28:
        cnt[1] = 1
    if cnt[2] > 19:
        cnt[2] = 1
print(total)