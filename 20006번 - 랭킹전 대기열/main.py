#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 20006                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: jieunb_b <boj.kr/u/jieunb_b>                +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/20006                          #+#        #+#      #+#     #
#    Solved: 2025/04/13 21:42:37 by jieunb_b      ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
input = sys.stdin.readline

p, m = map(int, input().split())
rooms = []
for _ in range(p): # O(300)
    player = input().strip().split()
    l, n = int(player[0]), player[1]
    # 모든 방 돌기
    entrace = False
    for room in rooms: # O(300)
        # 정원 찼는지 확인
        if len(room) != m:
        # 인원이 다 안찼을 경우 레벨 확인
            # 레벨이 된다면
            if room[0][0]-10<=l<=room[0][0]+10:
                room.append([l, n])
                entrace = True
                break
    if not entrace:
        rooms.append([[l, n]])

for room in rooms:
    if len(room) == m:
        print('Started!')
    else:
        print('Waiting!')
    room = sorted(room, key=lambda x: x[1])
    for player in room:
        print(*player)