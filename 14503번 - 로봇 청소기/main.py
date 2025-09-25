#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 14503                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: jieunb_b <boj.kr/u/jieunb_b>                +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/14503                          #+#        #+#      #+#     #
#    Solved: 2025/07/18 11:25:33 by jieunb_b      ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
r, c, d = map(int, input().split())
info = [list(map(int, input().split())) for _ in range(n)]
visited = [[0]*m for _ in range(n)]

dir = [(-1, 0), (0, 1), (1, 0), (0, -1)]

def search(r, c, d): 
    for _ in range(4):
        next_d = (4+d-1)%4 
        next_dir = dir[next_d] # (1, 0)
        next_r, next_c = r+next_dir[0], c+next_dir[1]
        if 0<=next_r<n and 0<=next_c<m and visited[next_r][next_c] == 0 and info[next_r][next_c] == 0:
            return [next_r, next_c, next_d]
        else:
            d = next_d
    return []

cur_r, cur_c, cur_d = r, c, d
count = 0
while(True):
    if visited[cur_r][cur_c] == 0:
        visited[cur_r][cur_c] = 1
        count += 1
    res = search(cur_r, cur_c, cur_d)
    if res:
        cur_r, cur_c, cur_d = res[0], res[1], res[2]
        continue
    else:
        prev_r, prev_c = cur_r-dir[cur_d][0], cur_c-dir[cur_d][1]
        if info[prev_r][prev_c] == 1:
            break
        else:
            cur_r, cur_c = prev_r, prev_c
print(count)


#＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃
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