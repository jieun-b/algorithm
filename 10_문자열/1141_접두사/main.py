#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 1141                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: jieunb_b <boj.kr/u/jieunb_b>                +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/1141                           #+#        #+#      #+#     #
#    Solved: 2024/10/10 00:13:11 by jieunb_b      ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
input = sys.stdin.readline

N = int(input())
all = []
for _ in range(N):
    all.append(input().rstrip())
all.sort(key=len)

count = 0
for i in range(N):
    flag = False
    for j in range(i+1, N):
        if all[j].startswith(all[i]):
            flag = True
            break
    if flag:
        count += 1

print(len(all)-count)