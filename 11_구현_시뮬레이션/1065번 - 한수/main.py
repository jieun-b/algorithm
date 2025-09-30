#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 1065                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: jieunb_b <boj.kr/u/jieunb_b>                +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/1065                           #+#        #+#      #+#     #
#    Solved: 2025/09/15 13:03:04 by jieunb_b      ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
input = sys.stdin.readline

n = int(input())

# 규칙이 있는거처럼 보이지만 다 확인해봐야 됨
# n이 최대 1000으로 작은 수이기 때문에 확인 가능할 듯

if n < 100:
    print(n)
else:
    cnt = 99
    for i in range(100, n+1): 
        a = str(i)
        if int(a[0])-int(a[1]) == int(a[1])-int(a[2]):
            cnt += 1
    print(cnt)