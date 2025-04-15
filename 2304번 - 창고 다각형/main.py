#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 2304                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: jieunb_b <boj.kr/u/jieunb_b>                +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/2304                           #+#        #+#      #+#     #
#    Solved: 2025/04/16 00:01:13 by jieunb_b      ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
input = sys.stdin.readline

n = int(input())

bars = dict()
for _ in range(n):
    l, h = map(int, input().split())
    bars[l] = h

visited = []
for i in range(max(bars)+1):
    if i in bars:
        visited.append(bars[i])
    else:
        visited.append(0)

max_height = max(bars, key=bars.get)
prev = 0
for i in range(max_height+1):
    if prev < visited[i]:
        prev = visited[i]
    visited[i] = prev
prev = 0
for i in range(len(visited)-1, max_height, -1):
    if prev < visited[i]:
        prev = visited[i]
    visited[i] = prev
print(sum(visited))