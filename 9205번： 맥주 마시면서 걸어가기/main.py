#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 9205                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: jieunb_b <boj.kr/u/jieunb_b>                +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/9205                           #+#        #+#      #+#     #
#    Solved: 2024/09/25 22:15:57 by jieunb_b      ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
from collections import deque
input = sys.stdin.readline

def search(h_x, h_y):
    queue = deque()
    queue.append((h_x, h_y))
    while(queue):
        x, y = queue.popleft()
        if abs(festival[0]-x) + abs(festival[1]-y) <= 1000:
            return print('happy')
        for i, c in enumerate(conve):
            if abs(c[0]-x) + abs(c[1]-y) <= 1000 and visited[i] == 0:
                queue.append((c[0], c[1]))
                visited[i] = 1
    return print('sad')

t = int(input())
for _ in range(t):
    n = int(input())
    conve = []
    house = list(map(int, input().split()))
    for _ in range(n):
        conve.append(list(map(int, input().split())))
    festival = list(map(int, input().split()))
    visited = [0 for _ in range(n)]
    search(house[0],house[1])
