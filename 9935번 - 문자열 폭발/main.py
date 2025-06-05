#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 9935                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: jieunb_b <boj.kr/u/jieunb_b>                +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/9935                           #+#        #+#      #+#     #
#    Solved: 2025/06/05 11:22:55 by jieunb_b      ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
input = sys.stdin.readline

q = list(input().strip())
x = list(input().strip())

a = []
for i in range(len(q)):
    a.append(q[i])
    if len(a) >= len(x) and a[-len(x):] == x:
        for _ in range(len(x)):
            a.pop()
if not a:
    print('FRULA')
else:
    print("".join(a))