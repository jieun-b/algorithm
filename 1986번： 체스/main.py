#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 1986                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: jieunb_b <boj.kr/u/jieunb_b>                +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/1986                           #+#        #+#      #+#     #
#    Solved: 2024/10/17 23:34:36 by jieunb_b      ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
queen = list(map(int, input().split()))
knight = list(map(int, input().split()))
pawn = list(map(int, input().split()))
board = [['' for _ in range(m)] for _ in range(n)]

count = 0
for k in range(queen[0]): 
    count += 1
    board[queen[1+k*2]-1][queen[2+k*2]-1] = 'Q' 
for k in range(knight[0]): 
    count += 1
    board[knight[1+k*2]-1][knight[2+k*2]-1] = 'K'
for k in range(pawn[0]):
    count += 1
    board[pawn[1+k*2]-1][pawn[2+k*2]-1] = 'P'

k_dir = ((2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2))
q_dir = ((0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, -1))

for i in range(n):
    for j in range(m):
        if board[i][j] == 'K':
            for r_dir, c_dir in k_dir:
                if 0<=i+r_dir<n and 0<=j+c_dir<m and board[i+r_dir][j+c_dir] == '':
                    count += 1
                    board[i+r_dir][j+c_dir] = 'X'
        if board[i][j] == 'Q':
            for r_dir, c_dir in q_dir: 
                for a in range(1, max(n,m)):
                    if not(0<=i+r_dir*a<n and 0<=j+c_dir*a<m) or not(board[i+r_dir*a][j+c_dir*a] == '' or board[i+r_dir*a][j+c_dir*a] == 'X'): # 변경된 위치
                        break
                    else:
                        if board[i+r_dir*a][j+c_dir*a] == '':
                            count += 1
                            board[i+r_dir*a][j+c_dir*a] = 'X'

print(n*m-count)          
# print(board)