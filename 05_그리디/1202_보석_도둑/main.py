#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 1202                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: jieunb_b <boj.kr/u/jieunb_b>                +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/1202                           #+#        #+#      #+#     #
#    Solved: 2025/07/02 16:52:09 by jieunb_b      ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
import heapq
input = sys.stdin.readline

n, k = map(int, input().split())

jew = [list(map(int, input().split())) for _ in range(n)]
bag = [int(input()) for _ in range(k)]

jew.sort(key=lambda x: (x[0], -x[1]))
bag.sort()

# 1. 최대한 비싼 보석 우선 
# 2. 무게가 큰 가방에 큰 보석을 넣는게 이득
# 각 가방에 담을 수 있는 최대 금액 찾기
# 큰 가방에 담을 수 있는 보석 개수보다 작은 가방에 담을 수 있는 보석 개수 결정하는 것이 더 적게 탐색
# 작은 가방부터 탐색 -> m이 c보다 같거나 작으면 가방에 담을 수 있는 후보로 저장 // 가장 가격 높은

idx = 0
heap = []
count = 0
for c in bag: # 작은 가방부터 큰 가방으로
    while(idx < n and jew[idx][0] <= c):
        heapq.heappush(heap, -jew[idx][1])
        idx += 1
    if heap:
        count += heapq.heappop(heap)
print(-count)