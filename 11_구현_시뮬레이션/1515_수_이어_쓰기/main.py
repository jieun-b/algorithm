#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 1515                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: jieunb_b <boj.kr/u/jieunb_b>                +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/1515                           #+#        #+#      #+#     #
#    Solved: 2025/04/09 20:57:13 by jieunb_b      ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
input = sys.stdin.readline

n_s = input().strip() # 남은 수를 이어붙인 수
n, idx = 0, 0 # N의 최솟값, n_s에서 찾을 숫자

while True:
    n += 1
    for s in str(n):
        if n_s[idx] == s:
            idx += 1
            if idx >= len(n_s):
                print(n)
                exit()