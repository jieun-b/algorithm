#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 7569                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: jieunb_b <boj.kr/u/jieunb_b>                +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/7569                           #+#        #+#      #+#     #
#    Solved: 2025/02/12 20:54:28 by jieunb_b      ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  
import sys
from collections import deque
from copy import deepcopy
input = sys.stdin.readline

m, n, h = map(int, input().split())

########## try 1
# 하루가 지나면 익은 토마토의 인접한 익지 않은 토마토는 익게 됨
# 며칠이 지나여 전체 토마토가 다 익는지 최소 일수

# def search(i, j, k):
#     queue = deque([(i, j, k)])
#     visited[i][j][k] = True
#     while queue:
#         z, y, x = queue.popleft()
#         for z_idx in range(3):
#             new_z = z + dz[z_idx]
#             for idx in range(4):
#                 new_x = x + dx[idx]
#                 new_y = y + dy[idx]
#                 if 0<=new_x<m and 0<=new_y<n and 0<=new_z<h:
#                     # 주위 토마토 중 익지 않은 토마토는 익도록 수정
#                     if graph[new_z][new_y][new_x] == 0:
#                         new_graph[new_z][new_y][new_x] = 1
#                     # 주위 익은 토마토 
#                     if graph[new_z][new_y][new_x] == 1 and visited[new_z][new_y][new_x] == False:
#                         queue.append((new_z, new_y, new_x))
#                         visited[new_z][new_y][new_x] = True

# dx = [1,0,-1,0]
# dy = [0,1,0,-1]
# dz = [0,1,-1]

# new_graph = []
# end = True
# for _ in range(h):
#     graph_tmp = []
#     for _ in range(n):
#         tmp = list(map(int, input().split()))
#         if 0 in tmp:
#             end = False
#         graph_tmp.append(tmp)    
#     new_graph.append(graph_tmp)

# if end:
#     print(0)
# else:
#     # 매번 리스트에 들어있는 1에 대해 탐색 수행..
#     count = 0
#     while True:
#         # 한번 돌 때마다 토마토 상자 업데이트 and 새로 방문
#         graph = deepcopy(new_graph)
#         visited = [[[False for _ in range(m)] for _ in range(n)] for _ in range(h)]
#         for i in range(h):
#             for j in range(n):
#                 for k in range(m):
#                     # 방문한적 없고 토마토가 익었을 때(1) 탐색
#                     if graph[i][j][k] == 1 and visited[i][j][k] == False:
#                         search(i, j, k)
#                     else:
#                         visited[i][j][k] = True
#         count += 1
#         if graph == new_graph:
#             break
#     if any(0 in graph_m for graph_nm in graph for graph_m in graph_nm):
#         print(-1)
#     else:
#         print(count)

# 처음에 모든 토마토를 큐에 넣기 queue
# 하나씩 빼면서 다음 턴에 처리할 토마토 넣기 new_queue

########## try 2
# dx = [1,0,-1,0]
# dy = [0,1,0,-1]
# dz = [0,1,-1]

# graph = []
# visited = []
# end = True
# queue = deque()
# for i in range(h):
#     graph_tmp = []
#     visited_tmp = []
#     for j in range(n):
#         tmp = list(map(int, input().split()))
#         graph_tmp.append(tmp)    
#         visited_tmp.append([False for _ in range(m)])
#         for k in range(len(tmp)):
#             if tmp[k] == 0:
#                 end = False
#             elif tmp[k] == 1:
#                 queue.append((i,j,k))
#                 visited_tmp[j][k] = True
#     graph.append(graph_tmp)
#     visited.append(visited_tmp)

# count = 0
# if end:
#     print(0)
# else:
#     while not end:
#         new_queue = deque()
#         if not queue:
#             break
#         while queue:
#             z, y, x = queue.popleft()
#             for z_idx in range(3):
#                 new_z = z + dz[z_idx]
#                 for idx in range(4):
#                     new_x = x + dx[idx]
#                     new_y = y + dy[idx]
#                     if 0<=new_x<m and 0<=new_y<n and 0<=new_z<h and visited[new_z][new_y][new_x] == False:
#                         if graph[new_z][new_y][new_x] == 0:
#                             graph[new_z][new_y][new_x] = 1
#                             new_queue.append((new_z,new_y,new_x))
#                             visited[new_z][new_y][new_x] = True
#         queue = deepcopy(new_queue)
#         count += 1
#     if any(0 in graph_m for graph_nm in graph for graph_m in graph_nm):
#         print(-1)
#     else:
#         print(count)


########## try 3
dx = [1, -1, 0, 0, 0, 0]
dy = [0, 0, 1, -1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]

graph = []
queue = deque()
for i in range(h):
    graph_tmp = []
    for j in range(n):
        tmp = list(map(int, input().split()))
        graph_tmp.append(tmp)    
        for k in range(len(tmp)):
            if tmp[k] == 1:
                queue.append((i,j,k))
    graph.append(graph_tmp)

count = -1
while queue:
    for _ in range(len(queue)):
        # queue안에 들어있는 처음 길이만큼만 탐색
        z, y, x = queue.popleft()
        for idx in range(6):
            new_z = z + dz[idx]
            new_y = y + dy[idx]
            new_x = x + dx[idx]
            if 0<=new_x<m and 0<=new_y<n and 0<=new_z<h and graph[new_z][new_y][new_x] == 0:
                graph[new_z][new_y][new_x] = 1
                # queue에 추가돼도 처음 정의한 길이만큼만 pop하기 때문에 다음 턴에 pop됨
                queue.append((new_z,new_y,new_x))
    count += 1

if any(0 in graph_m for graph_nm in graph for graph_m in graph_nm):
    print(-1)
else:
    print(count)