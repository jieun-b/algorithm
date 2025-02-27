#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 5212                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: jieunb_b <boj.kr/u/jieunb_b>                +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/5212                           #+#        #+#      #+#     #
#    Solved: 2024/08/27 22:03:07 by jieunb_b      ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
R, C = map(int, input().split())
now = []
for _ in range(R):
    now.append(list(str(input().strip())))
future = [['.']*C for _ in range(R)]

# X 주변에 .이 3개 이상이면 X->.
# 칸이 없어도 .의 개수로 포함
# 섬을 포함하는 위치 확인

x = [1,0,-1,0]
y = [0,1,0,-1]
min_y = R
max_y = 0
min_x = C
max_x = 0

for i in range(R):
    for j in range(C):
        if now[i][j] == 'X':
            count = 0
            for k in range(4):
                nx = j + x[k]
                ny = i + y[k]
                if not 0<=ny<R or not 0<=nx<C or now[ny][nx] == '.':
                    count += 1
            if count < 3:
                future[i][j] = 'X'
                min_y = min(min_y, i)
                max_y = max(max_y, i)
                min_x = min(min_x, j)
                max_x = max(max_x, j)
            
for i in range(min_y,max_y+1):
    print(*future[i][min_x:max_x+1], sep='')