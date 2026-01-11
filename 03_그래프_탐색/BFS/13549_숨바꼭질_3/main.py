#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 13549                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: jieunb_b <boj.kr/u/jieunb_b>                +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/13549                          #+#        #+#      #+#     #
#    Solved: 2025/05/24 15:49:17 by jieunb_b      ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
from collections import deque

input = sys.stdin.readline

n, k = map(int, input().split())

def search(start, end):
    queue = deque([(start, 0)])
    visited[start] = 0
    min_time = 100001
    while queue:
        pos, num = queue.popleft()
        if pos == end:
            min_time = min(min_time, num)
        for idx, value in enumerate([pos-1, pos+1, 2*pos]):
            if 0<=value<=100000:
                compare = num
                if idx != 2:
                    compare = num+1
                if visited[value] > compare:
                    queue.append((value, compare))
                    visited[value] = compare
    return min_time

visited = [100001] * 100001
print(search(n, k))