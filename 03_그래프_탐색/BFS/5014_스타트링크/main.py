#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 5014                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: jieunb_b <boj.kr/u/jieunb_b>                +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/5014                           #+#        #+#      #+#     #
#    Solved: 2024/08/15 23:27:08 by jieunb_b      ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
from collections import deque
input = sys.stdin.readline

F,S,G,U,D = map(int, input().split())

visited = [-1] * F # 전체 층

def search(S, G):
    queue = deque()
    queue.append(S)
    visited[S-1] += 1
    while(queue):
        position = queue.popleft() # 현재 위치
        if position == G:
            return visited[position-1]
        for next_position in (position + U, position - D):
            if 0<next_position<=F and visited[next_position-1] == -1:
                queue.append(next_position)
                visited[next_position-1] = visited[position-1] + 1

    return("use the stairs")

print(search(S, G))