#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 7682                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: jieunb_b <boj.kr/u/jieunb_b>                +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/7682                           #+#        #+#      #+#     #
#    Solved: 2025/05/27 16:16:53 by jieunb_b      ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
input = sys.stdin.readline

while(True):
    state = input().strip()
    if state == 'end':
        exit()
    
    res = 'valid'
    # 규칙에 어긋나는 경우
    count = state.count('X') - state.count('O')
    if not(count == 1 or count == 0):
        res = 'invalid'
    
    x, o = 0, 0
    if res == 'valid':
        # 가로, 세로, 대각선에 연속된 값들이 있는지 확인
        board = []
        for i in range(0, 9, 3):
            board.append(list(state[i:i+3]))

        # 가로
        for i in range(3):
            if board[i][0] == board[i][1] == board[i][2]:
                if board[i][0] == 'X':
                    x += 1
                elif board[i][0] == 'O':
                    o += 1
        # 세로
        for i in range(3):
            if board[0][i] == board[1][i] == board[2][i]:
                if board[0][i] == 'X':
                    x += 1
                elif board[0][i] == 'O':
                    o += 1
        # 대각선
        if board[0][0] == board[1][1] == board[2][2]:
            if board[0][0] == 'X':
                x += 1
            elif board[0][0] == 'O':
                o += 1
        if board[0][2] == board[1][1] == board[2][0]:
            if board[0][2] == 'X':
                x += 1
            elif board[0][2] == 'O':
                o += 1

    # 규칙 1. 연속된 값이 서로 다르게 나오면 안됨
    if x > 0 and o > 0:
        res = 'invalid'
    # 규칙 2. O가 연속될 때 X와 O의 개수 같아야 하고 X가 연속되면 X가 더 큼
    if (o == 1 and count == 1) or (x == 1 and count == 0):
        res = 'invalid'
    # 규칙 3. 연속된 값이 없는데 다 안찼으면 
    if x == 0 and o == 0 and state.count('.') != 0:
        res = 'invalid'
    
    print(res)