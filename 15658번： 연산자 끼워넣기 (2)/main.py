#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 15658                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: jieunb_b <boj.kr/u/jieunb_b>                +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/15658                          #+#        #+#      #+#     #
#    Solved: 2025/02/26 01:30:38 by jieunb_b      ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
input = sys.stdin.readline

n = int(input())
a_n = list(map(int, input().split()))
symbol = list(map(int, input().split()))

def operate(idx, res, value):
    if idx == 0:
        res = res + value
    elif idx == 1:
        res = res - value
    elif idx == 2:
        res = res * value
    else:
        if res < 0:
            res = -(abs(res) // value)
        else:
            res = res // value
    return res

def search(idx, res):
    if idx == n-1:
        res_list.append(res)
        return
    for i in range(4):
        if symbol[i] != 0:
            symbol[i] -= 1
            search(idx+1, operate(i, res, a_n[idx+1]))
            symbol[i] += 1

res_list = []
search(0, a_n[0]) 
res_list.sort() 
print(res_list[-1])
print(res_list[0])