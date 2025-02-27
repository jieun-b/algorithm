#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 1189                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: jieunb_b <boj.kr/u/jieunb_b>                +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/1189                           #+#        #+#      #+#     #
#    Solved: 2024/06/04 16:46:16 by jieunb_b      ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

R, C, K = list(map(int, input().split()))
txt = [str(input()) for _ in range(R)]
mat = [[0 for _ in range(C)] for _ in range(R)]
for i in range(R, 0, -1):
    for j in range(C):
        if txt[i-1][j] == 'T':
            mat[R-i][j] = 1

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]
num = []
def dfs(y,x):
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if 0<=ny<R and 0<=nx<C and mat[ny][nx] == 0:
            mat[ny][nx] = mat[y][x] + 1
            if ny == R-1 and nx == C-1:
                num.append(mat[ny][nx])
                mat[ny][nx] = 0
            else:
                dfs(ny,nx)
                mat[ny][nx] = 0
          
mat[0][0] = 1
dfs(0,0)
print(num.count(K))