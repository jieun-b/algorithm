#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 5972                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: jieunb_b <boj.kr/u/jieunb_b>                +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/5972                           #+#        #+#      #+#     #
#    Solved: 2025/05/26 16:27:47 by jieunb_b      ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
import heapq
input = sys.stdin.readline

n, m = map(int, input().split())

nodes =[[] for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    nodes[a].append((c, b)) # cost, num
    nodes[b].append((c, a))

INF = float('inf')
visited = [INF] * (n+1)
visited[1] = 0

heap = []
heapq.heappush(heap, (0, 1)) # cost, num

while heap:
    cur_cost, cur_node = heapq.heappop(heap)
    if visited[cur_node] < cur_cost:
        continue
    for cost, next_node in nodes[cur_node]:
        next_cost = cur_cost + cost
        if next_cost < visited[next_node]:
            visited[next_node] = next_cost
            heapq.heappush(heap, (next_cost, next_node))

print(visited[n])

# def search(num, cur):
#     global min_value
#     # 목표 헛간에 도착하면 종료
#     if num == n:
#         min_value = min(min_value, cur)
#         return
#     # 최소값보다 현재 값이 더 크면 종료
#     if min_value < cur:
#         return
#     # 현재 번호에서 연결된 노드 탐색하기
#     cur_list = nodes[num]
#     for i in range(len(cur_list)):
#         # 만약 방문했던 노드이면 건너뛰기
#         if visited[cur_list[i][0]] == 1:
#             continue
#         # 방문안했다면 값을 합하고 해당 노드로 넘어가기
#         visited[cur_list[i][0]] = 1
#         search(cur_list[i][0], cur+cur_list[i][1])
#         visited[cur_list[i][0]] = 0

# min_value = float('inf')
# visited = [0] * (n+1)
# visited[1] = 1
# search(1, 0)
# print(min_value)