#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 2178                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: jieunb_b <boj.kr/u/jieunb_b>                +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/2178                           #+#        #+#      #+#     #
#    Solved: 2025/02/11 21:43:24 by jieunb_b      ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
from collections import deque

# map은 문자열 요소를 특정 타입으로 변환하는 이터레이터
# 아래는 각 값을 언패킹해서 각각 할당해주는 예이고
# 하나씩 가져오려면 next를 사용
input = sys.stdin.readline
n, m = map(int, input().split())

# 최단 거리로 탐색하는 방법
# 갔던 길 다시 안가고 다 탐색해보기

graph = []
visited = []
for _ in range(n):
    graph.append(list(input().strip()))
    visited.append([0 for _ in range(len(graph[0]))])

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def search(i, j):
    queue = deque([(i, j)])
    visited[i][j] = 1
    while queue:
        y, x = queue.popleft()
        for k in range(4):
            new_y = y + dy[k]
            new_x = x + dx[k]
            if 0<=new_y<len(graph) and 0<=new_x<len(graph[0]):
                if visited[new_y][new_x] == 0 and graph[new_y][new_x] == '1':
                    visited[new_y][new_x] = visited[y][x]+1
                    queue.append((new_y, new_x))

search(0,0)
print(visited[n-1][m-1])