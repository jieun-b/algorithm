#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 25757                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: jieunb_b <boj.kr/u/jieunb_b>                +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/25757                          #+#        #+#      #+#     #
#    Solved: 2025/03/18 17:31:56 by jieunb_b      ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
input = sys.stdin.readline

# 윷놀이: 2, 같은 그림 찾기: 3, 원카드: 4
# 플레이 신청 횟수: N, 플레이할 게임 종류, 최대 몇 번의 게임?

n, game = input().split()
n = int(n)

players = {input().strip() for _ in range(n)}
if game == 'Y':
    print(len(players))
elif game == 'F':
    print(len(players) // 2)
else:
    print(len(players) // 3)