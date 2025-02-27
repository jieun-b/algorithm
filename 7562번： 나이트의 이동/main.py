#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 7562                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: jieunb_b <boj.kr/u/jieunb_b>                +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/7562                           #+#        #+#      #+#     #
#    Solved: 2024/05/26 22:36:11 by jieunb_b      ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
from collections import deque

move = [(2,1),(2,-1),(-2,1),(-2,-1),(1,2),(1,-2),(-1,2),(-1,-2)]
def bfs(current, target, l):
    queue = deque()
    queue.append(current)
    while queue:
        x, y = queue.popleft()   
        if (x, y) == target:
            return visited[x][y] 
        for i in move:
            nx = x + i[0]
            ny = y + i[1]
            if 0<=nx<l and 0<=ny<l and visited[nx][ny]==0:
                queue.append((nx,ny))
                visited[nx][ny] = visited[x][y] + 1

case = int(input())
results = []
for _ in range(case):
    l = int(input())
    current = tuple(map(int, input().split()))
    target = tuple(map(int, input().split()))
    
    visited = [[0] * l for _ in range(l)]
    results.append(bfs(current, target, l))

for result in results:
    print(result)