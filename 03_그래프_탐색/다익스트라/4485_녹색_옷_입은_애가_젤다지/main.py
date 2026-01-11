#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 4485                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: jieunb_b <boj.kr/u/jieunb_b>                +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/4485                           #+#        #+#      #+#     #
#    Solved: 2025/06/03 10:51:04 by jieunb_b      ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
import heapq
input = sys.stdin.readline

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def search(i, j, graph, sum_graph):
    queue = []
    heapq.heappush(queue, (graph[i][j], i, j))
    sum_graph[i][j] = graph[i][j]
    while(queue):
        cost, y, x = heapq.heappop(queue)
        for k in range(4):
            new_y = y + dy[k]
            new_x = x + dx[k]
            if 0<=new_y<n and 0<=new_x<n:
                if graph[new_y][new_x]+cost < sum_graph[new_y][new_x]:
                    heapq.heappush(queue, (graph[new_y][new_x]+cost, new_y, new_x))
                    sum_graph[new_y][new_x] = graph[new_y][new_x]+cost
    return sum_graph[-1][-1]

testcase = 0
INF = float('inf')
while(True):
    n = int(input())
    if n == 0:
        exit()
    testcase += 1
    graph = [list(map(int, input().split())) for _ in range(n)]
    sum_graph = [[INF]*n for _ in range(n)]
    answer = search(0, 0, graph, sum_graph)
    print(f"Problem {testcase}: {answer}")