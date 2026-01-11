#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 2580                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: jieunb_b <boj.kr/u/jieunb_b>                +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/2580                           #+#        #+#      #+#     #
#    Solved: 2025/02/28 22:17:26 by jieunb_b      ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
input = sys.stdin.readline
sudoku = [list(map(int, input().split())) for _ in range(9)]

# 줄을 돌면서 하나만 0이 있는 경우 남은 값 채우기
# 한 줄의 합을 45
# 빈칸만 저장하고 빈칸의 위치에서 가로, 세로, 정사각형 조건을 만족하는 수 넣기
zero = []
for i in range(9):
    for j in range(9):
        if sudoku[i][j] == 0:
            zero.append((i,j))

def row(y, a):
    for k in range(9):
        if sudoku[y][k] == a:
            return False
    return True
 
def col(x, a):
    for k in range(9):
        if sudoku[k][x] == a:
            return False
    return True

def rect(y,x,a):
    for i in range(3):
        for j in range(3):
            if a == sudoku[y // 3 * 3+i][x // 3 * 3+j]:
                return False
    return True

def search(idx):
    if idx == len(zero):
        for i in range(9):
            print(*sudoku[i])
        exit()
    for i in range(1, 10):
        y, x = zero[idx][0], zero[idx][1]
        if row(y, i) and col(x, i) and rect(y, x, i):
            sudoku[y][x] = i
            search(idx+1)
            sudoku[y][x] = 0

search(0)

# 리스트에서 개수세기 -> O(n)
# 가로 & 세로 O(nxm)
# for i in range(9):
#     zero_row, zero_col = -1, -1
#     row_sum, col_sum = 0, 0
#     for j in range(9):
#         row_sum += sudoku[i][j] # 가로 합
#         # col_sum += sudoku[j][i] # 세로 합
#         if sudoku[i][j] == 0: # 빈칸이 있는 경우
#             zero_row += 1
#         # if sudoku[j][i] == 0:
#         #     zero_col += 1
#     print(row_sum)
#     if zero_row == 1: # 0이 하나인 경우
#         sudoku[i][j] = 45-row_sum
    # if zero_col == 1: # 0이 하나인 경우
    #     sudoku[j][i] = 45-col_sum
    
# 정사각형
# (1,1), (4,4) (7,7), (1,4), (4,1), (1,7), (7,1), (4,7), (7,4) -> 0, 3, 6 / 0+3*i
# dirs = [(0,0), (0,1), (1,1), (1,0), (1,-1), (0,-1), (-1,-1), (-1,0), (-1,1)]
# for i in range(3):
#     for j in range(3):
#         zero_cnt, square_sum = 0, 0
#         zero_y, zero_x = -1,-1
#         for dir in dirs:
#             y, x = 1+3*i + dir[0], 1+3*j + dir[1]
#             square_sum += sudoku[y][x]
#             if sudoku[y][x] == 0:
#                 zero_cnt += 1
#                 zero_y, zero_x = y, x
#         if zero_cnt == 1:
#             sudoku[zero_y][zero_x] = 45-square_sum

# print(sudoku)