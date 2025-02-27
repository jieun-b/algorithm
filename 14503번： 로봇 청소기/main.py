#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 14503                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: jieunb_b <boj.kr/u/jieunb_b>                +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/14503                          #+#        #+#      #+#     #
#    Solved: 2025/02/14 22:24:14 by jieunb_b      ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
r, c, d = map(int, input().split())

states = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]

directions = {
    0: (-1,0),
    1: (0,1),
    2: (1,0),
    3: (0,-1),      
}

def move(r, c, d, count):
    check = False
    # 현재 칸의 주변 4칸 중 not visited가 있을 때
    for idx in range(4):
        new_d = (d+idx) % 4
        dr, dc = directions[new_d]
        new_r = r + dr
        new_c = c + dc
        if 1<=new_r<n-1 and 1<=new_c<m-1 and states[new_r][new_c] == 0 and not visited[new_r][new_c]:
            check = True
            visited[new_r][new_c] = True
            move(new_r, new_c, new_d, count+1)
    # 현재 칸의 주변 4칸이 전부 visited일 때
    if not check:
        new_d = (new_d+2) % 4
        dr, dc = directions[new_d]
        new_r = r + dr
        new_c = c + dc
        if 1<=new_r<n-1 and 1<=new_c<m-1 and states[new_r][new_c] == 0 and not visited[new_r][new_c]:
            visited[new_r][new_c] = True
            move(new_r, new_c, new_d, count+1)
        else:
            print(count)
            return

move(r, c, d, 1)