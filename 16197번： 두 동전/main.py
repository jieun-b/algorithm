#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 16197                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: jieunb_b <boj.kr/u/jieunb_b>                +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/16197                          #+#        #+#      #+#     #
#    Solved: 2025/02/26 21:25:16 by jieunb_b      ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
input = sys.stdin.readline

n, m = list(map(int, input().split()))
states = [list(input().strip()) for _ in range(n)]

dy = [0,1,0,-1]
dx = [1,0,-1,0]

coin = []
for i in range(n):
    for j in range(m):
        if states[i][j] == "o":
            coin.append((i,j))
        if len(coin) == 2:
            break

# 1. 보드를 다 돌면서 동전 위치 파악하기 nxm -> 20x20
# 2. 버튼을 계속 누르면서 최소 구하기 // 이미 최소보다 커지면 중단
# 3. 만약 두 동전을 이동시킬 위치가 둘다 인덱스를 벗어나는 위치이면 중단, 하나만 인덱스를 벗어나면 최솟값이랑 비교
# 4. 만약 두 동전을 이동시킬 위치에 #이 있으면 다음 동전만 이동  

min_num = 11

def search(current_num, coin_1, coin_2):
    global min_num
    if current_num == 11:
        return
    for k in range(4):
        # 이동할 좌표 정의
        coin_1_y, coin_1_x = coin_1[0]+dy[k], coin_1[1]+dx[k] 
        coin_2_y, coin_2_x = coin_2[0]+dy[k], coin_2[1]+dx[k]
        # 두 동전 모두 범위 밖
        if not (0<=coin_1_y<n and 0<=coin_1_x<m) and not (0<=coin_2_y<n and 0<=coin_2_x<m):
            continue
        # 한 동전만 범위 내
        if not (0<=coin_1_y<n and 0<=coin_1_x<m) or not (0<=coin_2_y<n and 0<=coin_2_x<m):
            min_num = min(min_num, current_num)
            return
        # 두 동전 모두 범위 내
        if 0<=coin_1_y<n and 0<=coin_1_x<m and states[coin_1_y][coin_1_x] == "#":
            coin_1_y, coin_1_x = coin_1
        if 0<=coin_2_y<n and 0<=coin_2_x<m and states[coin_2_y][coin_2_x] == "#":
            coin_2_y, coin_2_x = coin_2

        # 둘 다 제자리면 무시
        if (coin_1_y, coin_1_x) == coin_1 and (coin_2_y, coin_2_x) == coin_2:
            continue

        # 다음 상태 탐색
        search(current_num + 1, (coin_1_y, coin_1_x), (coin_2_y, coin_2_x))

search(1, coin[0], coin[1])
print(min_num if min_num <= 10 else -1)