#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 17144                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: jieunb_b <boj.kr/u/jieunb_b>                +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/17144                          #+#        #+#      #+#     #
#    Solved: 2025/07/20 13:28:34 by jieunb_b      ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
input = sys.stdin.readline

r, c, t = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(r)]

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

# 공기청정기 위치 찾기
air = []
for i in range(r):
    if a[i][0] == -1:
        air.append([i, 0])
        air.append([i+1, 0])
        break

# 미세먼지 확산
def diffuse(cur):
    next = [[0]*c for _ in range(r)]
    next[air[0][0]][air[0][1]], next[air[1][0]][air[1][1]] = -1, -1
    for i in range(r):
        for j in range(c):
            if cur[i][j] > 0:
                count = 0
                for k in range(4):
                    ni = i + di[k]
                    nj = j + dj[k]
                    if 0 <= ni < r and 0 <= nj < c and cur[ni][nj] != -1:
                        next[ni][nj] += cur[i][j] // 5
                        count += 1
                next[i][j] += cur[i][j] - (cur[i][j] // 5) * count
    return next

# 공기청정기 바람 이동
def move(cur):
    top, bottom = air[0][0], air[1][0]
    
    # 위쪽 반시계
    for i in range(top-1, 0, -1):
        cur[i][0] = cur[i-1][0]
    for j in range(0, c-1):
        cur[0][j] = cur[0][j+1]
    for i in range(0, top):
        cur[i][c-1] = cur[i+1][c-1]
    for j in range(c-1, 1, -1):
        cur[top][j] = cur[top][j-1]
    cur[top][1] = 0
    
    # 아래쪽 시계
    for i in range(bottom+1, r-1):
        cur[i][0] = cur[i+1][0]
    for j in range(0, c-1):
        cur[r-1][j] = cur[r-1][j+1]
    for i in range(r-1, bottom, -1):
        cur[i][c-1] = cur[i-1][c-1]
    for j in range(c-1, 1, -1):
        cur[bottom][j] = cur[bottom][j-1]
    cur[bottom][1] = 0

# T초 동안 시뮬레이션
for _ in range(t):
    a = diffuse(a)
    move(a)

# 남은 미세먼지 양 합산 (공기청정기 칸은 제외)
total = sum(sum(cell for cell in row if cell > 0) for row in a)
print(total)
