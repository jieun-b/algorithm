#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 11054                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: jieunb_b <boj.kr/u/jieunb_b>                +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/11054                          #+#        #+#      #+#     #
#    Solved: 2025/07/28 22:15:24 by jieunb_b      ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
inc = [1]*n
dec = [1]*n

# i가 s_k일 때 왼쪽 증가하는 수열의 최대 길이
for i in range(n):
    for j in range(i):
        # 값이 a[i] 보다 작아야 됨
        if a[j] < a[i]:
            inc[i] = max(inc[i], inc[j]+1)

for i in range(n-1, -1, -1):
    for j in range(n-1, i, -1):
        # 값이 a[i] 보다 작아야 됨
        if a[j] < a[i]:
            dec[i] = max(dec[i], dec[j]+1)

res = 0
for i in range(n):
    res = max(res, inc[i]+dec[i]-1)
print(res)