#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 1260                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: jieunb_b <boj.kr/u/jieunb_b>                +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/1260                           #+#        #+#      #+#     #
#    Solved: 2025/02/11 22:29:31 by jieunb_b      ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
# import sys
# from collections import deque

# input = sys.stdin.readline

# n, m, v = map(int, input().split())

# relations = []
# visited_dfs = []
# visited_bfs = []
# for _ in range(n+1):
#     relations.append([])
#     visited_dfs.append(False)
#     visited_bfs.append(False)

# for _ in range(m):
#     v1, v2 = map(int, input().split())
#     relations[v1].append(v2)
#     relations[v2].append(v1)

# path_dfs = []
# path_bfs = []

# def dfs(start):
#     path_dfs.append(start)
#     visited_dfs[start] = True
#     relation = sorted(relations[start])
#     # 현재 정점과 연결된 다른 정점 중 visited 안한 경우 방문하도록
#     for vertex in relation:
#         if visited_dfs[vertex] == False:
#             dfs(vertex)

# def bfs(start):
#     queue = deque([start])
#     visited_bfs[start] = True
#     while queue:
#         current = queue.popleft()
#         path_bfs.append(current)
#         relation = sorted(relations[current])
#         for vertex in relation:
#             if visited_bfs[vertex] == False:
#                 queue.append(vertex)
#                 visited_bfs[vertex] = True
# dfs(v)
# print(*path_dfs)

# bfs(v)
# print(*path_bfs)


import sys
from collections import deque
input = sys.stdin.readline

n, m, v = map(int, input().split())
linked = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    linked[a].append(b)
    linked[b].append(a)
for nodes in linked:
    nodes.sort()

def dfs(v, visited):
    visited[v] = True
    res_dfs.append(v)
    for i in range(len(linked[v])):
        next = linked[v][i]
        if not visited[next]:
            dfs(next, visited)

def bfs(v, visited):
    queue = deque([v])
    visited[v] = True
    res_bfs.append(v)
    while queue:
        cur = queue.popleft()
        for i in range(len(linked[cur])):
            next = linked[cur][i]
            if not visited[next]:
                queue.append(next)
                res_bfs.append(next)
                visited[next] = True

res_dfs = []
res_bfs = []
dfs(v, [False] * (n+1))
bfs(v, [False] * (n+1))
print(*res_dfs)
print(*res_bfs)