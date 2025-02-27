#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 1697                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: jieunb_b <boj.kr/u/jieunb_b>                +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/1697                           #+#        #+#      #+#     #
#    Solved: 2024/08/15 21:49:37 by jieunb_b      ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
from collections import deque
input = sys.stdin.readline

N, K = map(int, input().split())
visited = [0 for i in range(100001)]

def search(N,K):
    queue = deque()
    queue.append(N)

    while(queue):
        position = queue.popleft()
        if position == K:
            return visited[position]
        for next_position in (position + 1, position - 1, position * 2):
            if 0<=next_position<=100000 and visited[next_position] == 0:
                queue.append(next_position)
                visited[next_position] = visited[position] + 1

print(search(N,K))