#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 7490                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: jieunb_b <boj.kr/u/jieunb_b>                +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/7490                           #+#        #+#      #+#     #
#    Solved: 2024/09/18 19:17:54 by jieunb_b      ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
input = sys.stdin.readline

n = int(input())
testcase = []
for _ in range(n):
    testcase.append(int(input()))

def cal(idx,res):
    if idx == len(num):
        if eval(res.replace(" ","")) == 0:
            print(res)
        return
    # space
    tmp = res + ' ' + str(num[idx])
    cal(idx+1, tmp)
    # +
    tmp = res + '+' + str(num[idx])
    cal(idx+1, tmp)
    # -
    tmp = res + '-' + str(num[idx])
    cal(idx+1, tmp)

for i in range(len(testcase)):
    num = [n+1 for n in range(testcase[i])]
    cal(1,'1')
    if i != len(testcase)-1: print()