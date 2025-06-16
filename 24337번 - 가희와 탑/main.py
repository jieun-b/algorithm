#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 24337                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: jieunb_b <boj.kr/u/jieunb_b>                +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/24337                          #+#        #+#      #+#     #
#    Solved: 2025/06/16 17:37:15 by jieunb_b      ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
input = sys.stdin.readline

n, a, b = map(int, input().split())

if a+b > n+1:
    print(-1)
    exit(0)

if a == 1:
    result = [b]
    for i in range(n-b):
        result.append(1)
    for i in range(b-1, 0, -1):
        result.append(i)
elif b == 1:
    result = [1 for i in range(n-a)]
    for i in range(1, a+1):
        result.append(i)
else:
    if a > b:
        result = [1 for i in range(n-(a+b-1))]
        for i in range(1, a+1):
            result.append(i)
        for i in range(b-1, 0, -1):
            result.append(i)
    else:
        result = [1 for i in range(n-(a+b-1))]
        for i in range(1, a):
            result.append(i)
        for i in range(b, 0, -1):
            result.append(i)
print(*result)