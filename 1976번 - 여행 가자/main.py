#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 1976                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: jieunb_b <boj.kr/u/jieunb_b>                +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/1976                           #+#        #+#      #+#     #
#    Solved: 2025/06/06 09:46:11 by jieunb_b      ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
m = int(input())

graph = [[] for _ in range(n+1)]
visited = [False for _ in range(n+1)]

for i in range(n):
    info = list(map(int, input().split()))
    for j in range(n):
        if info[j] == 1:
            graph[i+1].append(j+1)
        
plan = list(map(int, input().split()))
start = plan[0]
plan = set(plan)

def search(start):
    queue = deque([start])
    visited[start] = True
    plan.remove(start)
    while(queue):
        i = queue.popleft()
        for j in range(len(graph[i])):
            if not visited[graph[i][j]]:
                queue.append(graph[i][j])
                visited[graph[i][j]] = True
                if graph[i][j] in plan:
                    plan.remove(graph[i][j])
    if plan:
        return 'NO'
    else:
        return 'YES'

print(search(start))