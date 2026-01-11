#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 1987                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: jieunb_b <boj.kr/u/jieunb_b>                +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/1987                           #+#        #+#      #+#     #
#    Solved: 2025/02/28 22:18:04 by jieunb_b      ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
input = sys.stdin.readline

r,c = list(map(int, input().split()))
board = [list(input().strip()) for _ in range(r)]

# 보드 체크 20x20
# 보드에 등장한 모든 알파벳 저장
alphabet = set(board[0][0])

dx = [1,0,-1,0]
dy = [0,1,0,-1]

def search(i,j,num):
    # 어디든 막히면 종료
    global max_num
    max_num = max(max_num, num)
    for k in range(4):
        y, x = i+dy[k], j+dx[k]
        if 0<=y<r and 0<=x<c and board[y][x] not in alphabet:
            alphabet.add(board[y][x])
            search(y,x,num+1)
            alphabet.remove(board[y][x])

max_num = 0
search(0,0,1)
print(max_num)