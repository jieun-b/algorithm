#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 15649                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: jieunb_b <boj.kr/u/jieunb_b>                +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/15649                          #+#        #+#      #+#     #
#    Solved: 2025/09/24 15:59:33 by jieunb_b      ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
# import sys
# from itertools import permutations
# input = sys.stdin.readline

# n, m = map(int, input().split())

# all_num = [i+1 for i in range(n)]
# res = [p for p in permutations(all_num, m)]
# for r in res:
#     print(*r)

import sys
input = sys.stdin.readline
n, m = map(int, input().split())

all_num = set()
visited = [False] * (n+1)

def search(cur, made):
    if cur == m:
        all_num.add(tuple(made))
    for i in range(1, n+1):
        if not visited[i]:
            made.append(i)
            visited[i] = True
            search(cur+1, made)
            visited[i] = False
            made.pop()

search(0, [])
all_num = sorted(all_num)
for num in all_num:
    print(*num)