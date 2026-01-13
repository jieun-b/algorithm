#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 14891                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: jieunb_b <boj.kr/u/jieunb_b>                +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/14891                          #+#        #+#      #+#     #
#    Solved: 2026/01/12 22:35:32 by jieunb_b      ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
from collections import deque
input = sys.stdin.readline

# 톱니바퀴의 상태 / 12시 방향부터 시계 방향
wheels = [deque(list(map(int, input().strip()))) for _ in range(4)]
# 회전 횟수
k = int(input())
# 회전 방법
info = [list(map(int, input().split())) for _ in range(k)]

# 회전 함수 정의
def left(idx, dir):
    if idx < 0:
        return
    if wheels[idx][2] != wheels[idx+1][6]:
        left(idx-1, -dir)
        wheels[idx].rotate(dir)

def right(idx, dir):
    if idx > 3:
        return
    if wheels[idx][6] != wheels[idx-1][2]:
        right(idx+1, -dir)
        wheels[idx].rotate(dir)

# 회전 시작
for idx, dir in info:
    idx -= 1
    left(idx-1, -dir)
    right(idx+1, -dir)
    wheels[idx].rotate(dir)

# 최종 결과는 각 톱니 바퀴의 idx=0의 값 * 2**idx
res = 0
for i in range(4):
    res += wheels[i][0] * (2**i)
print(res)