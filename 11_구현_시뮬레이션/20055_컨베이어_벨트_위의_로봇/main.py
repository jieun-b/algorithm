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

# 벨트 회전은 push/pop으로 실행
# 벨트가 회전할 때 리스트도 자르고 추가하기

# 벨트 위의 상태는 리스트로 저장
# 로봇 이동
# 내구도가 0인 칸의 정보는 계속 기록

n, k = map(int, input().split())
belt = deque(map(int, input().split()))
robot = [False]*n

zero = 0
step = 0
while(True):
    step += 1
    # 벨트, 로봇 회전
    belt.rotate(1)
    robot.pop()
    robot.insert(0, False)
    robot[-1] = False
    # 로봇 이동, 이동하는 경우 내구도 감소
    for i in range(n-2, -1, -1):
        if robot[i] and not robot[i+1] and belt[i+1] > 0:
            robot[i], robot[i+1] = False, True
            belt[i+1] -= 1
            if belt[i+1] == 0:
                zero += 1
    robot[-1] = False
    # 로봇 올리기 
    if belt[0] > 0:
        robot[0] = True
        belt[0] -= 1
        if belt[0] == 0:
            zero += 1
    if zero >= k:
        break

print(step)