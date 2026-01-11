#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 1417                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: jieunb_b <boj.kr/u/jieunb_b>                +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/1417                           #+#        #+#      #+#     #
#    Solved: 2025/09/24 18:33:11 by jieunb_b      ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
import heapq
input = sys.stdin.readline

n = int(input())
dasom = int(input())

if n == 1:
    print(0)
    exit()
    
heap = []
for _ in range(n-1):
    heapq.heappush(heap, -int(input()))

count = 0
while -heap[0] >= dasom:
    count += 1
    num = -heapq.heappop(heap) - 1
    dasom += 1
    heapq.heappush(heap, -num)
print(count)