#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 1238                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: jieunb_b <boj.kr/u/jieunb_b>                +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/1238                           #+#        #+#      #+#     #
#    Solved: 2025/06/17 17:16:52 by jieunb_b      ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
import heapq
input = sys.stdin.readline

n, m, x = map(int, input().split())
forward = [[] for _ in range(n+1)] # home -> x
backward = [[] for _ in range(n+1)] # x -> home
for _ in range(m):
    start, end, time = map(int, input().split())
    forward[start].append((time, end))
    backward[end].append((time, start))

INF = float('inf')

def search(info, start):
    min_list = [INF for _ in range(n+1)]
    heap = []
    heapq.heappush(heap, (0, start))
    while(heap):
        cur_time, cur = heapq.heappop(heap)
        for time, next in info[cur]:
            next_time = cur_time+time
            if min_list[next] > next_time:
                min_list[next] = next_time
                heapq.heappush(heap, (next_time, next))
    return min_list

# home -> x
first = search(backward, x)
# x -> home
second = search(forward, x)

res = 0
for i in range(1, n+1):
    if i != x:
        res = max(res, first[i]+second[i])
print(res)