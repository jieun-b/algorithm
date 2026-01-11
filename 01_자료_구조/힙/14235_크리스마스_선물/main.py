#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 14235                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: jieunb_b <boj.kr/u/jieunb_b>                +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/14235                          #+#        #+#      #+#     #
#    Solved: 2025/10/12 00:24:33 by jieunb_b      ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
import heapq
input = sys.stdin.readline

n = int(input())
heap = []
for i in range(n):
    info = list(map(int, input().split()))
    if info[0] == 0: 
        if heap != []:
            value = heapq.heappop(heap)
            print(-value)
        else:
            print(-1)
    else: 
        for k in range(1, info[0]+1):
            heapq.heappush(heap, -info[k])