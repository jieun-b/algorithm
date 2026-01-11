#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 4574                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: jieunb_b <boj.kr/u/jieunb_b>                +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/4574                           #+#        #+#      #+#     #
#    Solved: 2025/02/28 22:17:43 by jieunb_b      ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
input = sys.stdin.readline

# U: 도미노에 쓰여 있는 한 숫자
# LU: 길이가 2인 문자열, U의 위치
# V: 도미노에 쓰여 있는 다른 숫자
# LV: 길이가 2인 문자열, V의 위치

def row(k, i):
    for x in range(9):
        if sudoku[i][x] == k:
            return False
    return True

def col(k, j):
    for y in range(9):
        if sudoku[y][j] == k:
            return False
    return True

def rect(k, i, j):
    for y in range(3):
        for x in range(3):
            if sudoku[i // 3 * 3+y][j // 3 * 3+x] == k: 
                return False
    return True

dx = [1, 0]
dy = [0, 1]

def search(idx): # 현재 위치
    # 가능한 숫자 넣어보기
    global solved
    # 다 채웠으면 종료
    if idx == len(zero):
        print('Puzzle', count)
        for i in range(9):
            tmp = ""
            for j in range(9):
                tmp += str(sudoku[i][j])
            print(tmp)
        solved = True
        return
    
    # 빈 칸에서 도미노 넣어보기
    i, j = zero[idx]
    # 빈 칸이 아니면 리턴
    if sudoku[i][j] != 0:
        search(idx+1)
        return
    # 첫 번째 값 넣기
    for k in range(1, 10):
        if row(k, i) and col(k, j) and rect(k, i, j):
            for d in range(2):
                y, x = i + dy[d], j + dx[d]
                if 0<=y<9 and 0<=x<9 and sudoku[y][x] == 0:
                    for l in range(1, 10):
                        if k != l and row(l, y) and col(l, x) and rect(l, y, x) and not used[k][l]:
                            sudoku[i][j], sudoku[y][x] = k, l
                            used[k][l] = used[l][k] = True
                            search(idx + 1)
                            if solved:
                                return
                            sudoku[i][j] = sudoku[y][x] = 0
                            used[k][l] = used[l][k] = False

dic = {'A':0, 'B':1, 'C':2, 'D':3, 'E':4, 'F':5, 'G':6,'H':7, 'I':8}

count = 1
while True:
    n = int(input())
    if n == 0:
        break
    # 스도쿠 초기화
    sudoku = [[0]*9 for _ in range(9)]
    used = [[False]*10 for _ in range(10)] # 숫자 쌍에 대한 사용 여부
    for _ in range(n):
        tmp = input().split()
        sudoku[dic[tmp[1][0]]][int(tmp[1][1])-1] = int(tmp[0])
        sudoku[dic[tmp[3][0]]][int(tmp[3][1])-1] = int(tmp[2])
        used[int(tmp[0])][int(tmp[2])] = used[int(tmp[2])][int(tmp[0])] = True
    num = input().split()
    for i in range(9):
        sudoku[dic[num[i][0]]][int(num[i][1])-1] = i+1
    
    # 빈 칸 체크
    zero = [(i, j) for i in range(9) for j in range(9) if sudoku[i][j] == 0]
    solved = False
    search(0)

    count += 1