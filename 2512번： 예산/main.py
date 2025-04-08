#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 2512                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: jieunb_b <boj.kr/u/jieunb_b>                +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/2512                           #+#        #+#      #+#     #
#    Solved: 2025/04/08 17:18:15 by jieunb_b      ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
input = sys.stdin.readline

n = int(input())
ns = sorted(list(map(int, input().split())))
m = int(input())

result = ns[-1]
for i in range(n):
    if ns[i]*(n-i) <= m:
        m = m-ns[i]
    else: 
        result = m//(n-i)
        break
print(result)