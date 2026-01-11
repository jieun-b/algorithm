#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 2644                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: jieunb_b <boj.kr/u/jieunb_b>                +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/2644                           #+#        #+#      #+#     #
#    Solved: 2024/05/20 22:12:25 by jieunb_b      ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

n = int(input()) # 전체 사람 수
a, b = list(map(int, input().split())) # 계산할 사람의 번호
m = int(input()) # 부모 자식 간의 관계 수

graph = [[] for _ in range(n+1)]
for _ in range(m):
    x, y = list(map(int, input().split())) # 부모, 자식 번호
    graph[x].append(y)
    graph[y].append(x)

visited = [0] * (n+1)

def dfs(graph, visited, a, b):
    if a == b:
        print(visited[a])
    for i in graph[a]:
        if visited[i] == 0:
            visited[i] = visited[a]+1
            dfs(graph, visited, i, b)
            
dfs(graph, visited, a, b)

if visited[b] == 0:
    print(-1)