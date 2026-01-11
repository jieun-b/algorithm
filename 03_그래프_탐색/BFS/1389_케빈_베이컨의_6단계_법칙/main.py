#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 1389                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: jieunb_b <boj.kr/u/jieunb_b>                +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/1389                           #+#        #+#      #+#     #
#    Solved: 2024/05/21 01:15:30 by jieunb_b      ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

from collections import deque

N, M = list(map(int, input().split())) # 유저 수, 친구 관계 수
graph = [[] for _ in range(N+1)]
for _ in range(M): # 친구 관계
    A, B = list(map(int, input().split()))
    graph[A].append(B)
    graph[B].append(A)

def bfs(graph, visited, i, j):
    queue = deque([i])
    visited[i] += 1
    while queue:
        v = queue.popleft()
        if v == j:
            return visited[v]-1
        for k in graph[v]:
            if visited[k] == 0:
                visited[k] = visited[v] + 1
                queue.append(k)

sum = [0] * (N+1)
sum[0] = 999999
for i in range(1,N+1): # 케빈 베이컨의 수를 계산할 사람
    for j in range(1, N+1): # 연결된 사람 
        visited = [0] * (N+1) 
        if i != j:
            count = bfs(graph, visited, i, j)
            sum[i] += count
            
print(sum.index(min(sum)))