#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 2668                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: jieunb_b <boj.kr/u/jieunb_b>                +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/2668                           #+#        #+#      #+#     #
#    Solved: 2025/05/27 18:54:43 by jieunb_b      ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
input = sys.stdin.readline

n = int(input())
first = [i+1 for i in range(n)]
second = [int(input()) for _ in range(n)]

def search(target, i, cycle):
    if i == target:
        return cycle
    if visited[i]:
        return []
    cycle.append(i+1)
    visited[i] = True
    return search(target, second[i]-1, cycle)

res = []
for i in range(n): 
    visited = [False] * n
    cycle = search(i, second[i]-1, [i+1]) 
    res.extend(cycle)

res = sorted(set(res))
print(len(res))
for num in res:
    print(num)