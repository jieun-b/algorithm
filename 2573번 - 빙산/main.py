#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 2573                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: jieunb_b <boj.kr/u/jieunb_b>                +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/2573                           #+#        #+#      #+#     #
#    Solved: 2025/09/23 22:44:54 by jieunb_b      ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def search(i, j):
    queue = deque([(i, j)])
    visited.add((i, j))
    minus = {}
    while queue:
        # 현재 위치
        i, j = queue.popleft()
        h = 0
        for k in range(4):
            new_i = i + dy[k]
            new_j = j + dx[k]
            if 0<=new_i<n and 0<=new_j<m: # 갈 수 있는 곳인지 확인
                if graph[new_i][new_j] == 0: # 바닷물인지 확인
                    h += 1
                else: # 바닷물이 아니라면 다음 갈 곳으로 정하기
                    if (new_i, new_j) not in visited:
                        queue.append((new_i, new_j))
                        visited.add((new_i, new_j))
        minus[(i, j)] = h
    return minus

pos = [(i, j) for i in range(n) for j in range(m) if graph[i][j] > 0]
time = 0
while True:
    # 만약 전체 순회했는데 모두 0이면 0
    cnt = 0
    visited = set()
    # 빙산이 있는 좌표 순회
    for i, j in pos:
        # 방문 안한 경우만 bfs
        if (i,j) not in visited:
            cnt += 1
            minus = search(i, j)
        if cnt > 1:
            print(time)
            exit()
    # 순회 후 덩어리가 1보다 증가했으면 종료 or 순회 후 덩어리가 0이면 분리되기 전에 다 녹아 종료
    if cnt == 0:  
        print(0)
        exit()
    # 그래프 갱신
    new_pos = []
    for i, j in pos:
        graph[i][j] = max(0, graph[i][j]-minus[(i,j)])
        if graph[i][j] > 0:
            new_pos.append((i, j))
    pos = new_pos
    time += 1