#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 1430                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: jieunb_b <boj.kr/u/jieunb_b>                +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/1430                           #+#        #+#      #+#     #
#    Solved: 2024/09/04 23:04:06 by jieunb_b      ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
input = sys.stdin.readline
N, R, D, X, Y = map(int(input().split())) # 탑의 개수, 사정 거리, 초기 에너지, 적의 X좌표, Y좌표
tower = []
for i in range(N):
    x, y = map(int(input().split()))
    tower.append([x, y])

# 적과 사정 거리 안에 있는 탑 개수 확인
# 탑과 사정 거리 안에 있는 다른 탑 확인