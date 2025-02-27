#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 20055                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: jieunb_b <boj.kr/u/jieunb_b>                +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/20055                          #+#        #+#      #+#     #
#    Solved: 2024/09/25 22:56:18 by jieunb_b      ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
from collections import deque
input = sys.stdin.readline

N, K = map(int, input().split())
A = list(map(int, input().split()))

a = deque()
robot = deque()
for i in range(len(A)-1,-1,-1):
    a.append(A[i])
for _ in range(N):
    robot.append(0)

count = 0
while(True):
    # step 1
    tmp = a.popleft()
    a.append(tmp)
    robot.popleft()
    robot.append(0)
    robot[0] = 0
    # step 2
    for i in range(1,N):
        if robot[i] == 1:
            if robot[i-1] == 0 and a[i+N-1] > 0:
                robot[i-1] = 1
                robot[i] = 0
                a[i+N-1] = a[i+N-1] - 1
    robot[0] = 0
    # step 3
    if a[-1] != 0:
        robot[-1] = 1
        a[-1] = a[-1] - 1
    # step 4
    count += 1
    zero = a.count(0)
    if zero >= K:
        break
print(count)