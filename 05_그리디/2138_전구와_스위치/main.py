#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 2138                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: jieunb_b <boj.kr/u/jieunb_b>                +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/2138                           #+#        #+#      #+#     #
#    Solved: 2025/05/30 23:36:20 by jieunb_b      ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
import copy
input = sys.stdin.readline

n = int(input())
cur = list(map(int, input().strip()))
tar = list(map(int, input().strip()))

cur1 = copy.deepcopy(cur)
cur2 = copy.deepcopy(cur)

def toggle(arr, i):
    for j in [i-1, i, i+1]:
        if 0 <= j < len(arr):
            arr[j] = 1 - arr[j]

# case1
case1 = 0
for i in range(1, n):
    if cur1[i-1] != tar[i-1]:
        toggle(cur1, i)
        case1 += 1
if cur1 != tar:
    case1 = -1    

# case2
case2 = 1
toggle(cur2, 0)

for i in range(1, n):
    if cur2[i-1] != tar[i-1]:
        toggle(cur2, i)
        case2 += 1
if cur2 != tar:
    case2 = -1  

if case1 == -1:
    print(case2)
elif case2 == -1:
    print(case1)
else:
    print(min(case1, case2))