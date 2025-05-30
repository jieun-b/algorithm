#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 13335                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: jieunb_b <boj.kr/u/jieunb_b>                +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/13335                          #+#        #+#      #+#     #
#    Solved: 2025/05/29 20:47:58 by jieunb_b      ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
from collections import deque
input = sys.stdin.readline

n, w, l = map(int, input().split())
a = list(map(int, input().split()))

queue = deque(a)
bridge = deque([0]*w)
count = 0
while(bridge):
    bridge.popleft()
    if queue:
        if sum(bridge)+queue[0] <= l:
            bridge.append(queue.popleft())
        else:
            bridge.append(0)
    count += 1
print(count)