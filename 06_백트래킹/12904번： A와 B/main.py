#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 12904                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: jieunb_b <boj.kr/u/jieunb_b>                +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/12904                          #+#        #+#      #+#     #
#    Solved: 2024/10/10 00:14:01 by jieunb_b      ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

import sys

sys.setrecursionlimit(10**7)
input = sys.stdin.readline

# S에 두 가지 연산을 해서 T와 같은지 확인
S = input().rstrip()
T = input().rstrip()

def check(old): 
    global res
    if old == S:
        res = 1
        return
    if len(old) < len(S):
        return
  
    if old[-1] == 'A':
        old = old[:-1]
        check(old)
    else:
        old = old[:-1]
        old = old[::-1]
        check(old)

res = 0
check(T)
print(res)



