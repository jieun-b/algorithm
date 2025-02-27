#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 1195                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: jieunb_b <boj.kr/u/jieunb_b>                +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/1195                           #+#        #+#      #+#     #
#    Solved: 2024/09/04 23:02:02 by jieunb_b      ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
input = sys.stdin.readline
long = list(map(int, input().rstrip()))
short = list(map(int, input().rstrip()))

if len(short) > len(long):
    long, short = short, long

count = 0
for i in range(len(short)):
    flag = True
    for j in range(i+1):
        if short[j] == 2 and long[j-i-1] == 2:
            flag = False
            break
    if flag:
        count = max(count, i+1)
    flag = True
    for j in range(i+1):
        if short[j-i-1] == 2 and long[j] == 2:
            flag = False
            break
    if flag:
        count = max(count, i+1)

for i in range(len(long)-len(short)+1):
    flag = True
    for j in range(len(short)):
        if short[j] == 2 and long[i+j] == 2:
            flag = False
            break
    
    if flag:
        count = max(count, len(short))
    
print(len(short) + len(long) - count)

