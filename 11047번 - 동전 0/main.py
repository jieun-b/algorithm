#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 11047                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: jieunb_b <boj.kr/u/jieunb_b>                +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/11047                          #+#        #+#      #+#     #
#    Solved: 2025/09/15 13:02:50 by jieunb_b      ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
a = [int(input()) for _ in range(n)]

cnt = 0
for i in range(n-1, -1, -1):
    if a[i] > k:
        continue
    cnt += k // a[i]
    k = k % a[i]
print(cnt)