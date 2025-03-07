#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 12100                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: jieunb_b <boj.kr/u/jieunb_b>                +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/12100                          #+#        #+#      #+#     #
#    Solved: 2025/03/06 12:57:43 by jieunb_b      ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
from copy import deepcopy
input = sys.stdin.readline 

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]

# 블록을 위로 이동
def up(board):
    new_board = [[0] * n for _ in range(n)]
    for j in range(n):
        temp = []
        for i in range(n):
            if board[i][j]:
                temp.append(board[i][j])
        
        merged = []
        i = 0
        while i < len(temp):
            if i < len(temp) - 1 and temp[i] == temp[i + 1]:  
                merged.append(temp[i] * 2)
                i += 2
            else:
                merged.append(temp[i])
                i += 1
        
        for i in range(len(merged)):
            new_board[i][j] = merged[i]
    
    return new_board

# 블록을 아래로 이동
def down(board):
    new_board = [[0] * n for _ in range(n)]
    for j in range(n):
        temp = []
        for i in range(n - 1, -1, -1):
            if board[i][j]:
                temp.append(board[i][j])
        
        merged = []
        i = 0
        while i < len(temp):
            if i < len(temp) - 1 and temp[i] == temp[i + 1]:  
                merged.append(temp[i] * 2)
                i += 2
            else:
                merged.append(temp[i])
                i += 1
        
        for i in range(len(merged)):
            new_board[n - 1 - i][j] = merged[i]
    
    return new_board

# 블록을 왼쪽으로 이동
def left(board):
    new_board = [[0] * n for _ in range(n)]
    for i in range(n):
        temp = []
        for j in range(n):
            if board[i][j]:
                temp.append(board[i][j])
        
        merged = []
        j = 0
        while j < len(temp):
            if j < len(temp) - 1 and temp[j] == temp[j + 1]:  
                merged.append(temp[j] * 2)
                j += 2
            else:
                merged.append(temp[j])
                j += 1
        
        for j in range(len(merged)):
            new_board[i][j] = merged[j]
    
    return new_board

# 블록을 오른쪽으로 이동
def right(board):
    new_board = [[0] * n for _ in range(n)]
    for i in range(n):
        temp = []
        for j in range(n - 1, -1, -1):
            if board[i][j]:
                temp.append(board[i][j])
        
        merged = []
        j = 0
        while j < len(temp):
            if j < len(temp) - 1 and temp[j] == temp[j + 1]:  
                merged.append(temp[j] * 2)
                j += 2
            else:
                merged.append(temp[j])
                j += 1
        
        for j in range(len(merged)):
            new_board[i][n - 1 - j] = merged[j]
    
    return new_board

# 최대 5번 이동하면서 최대 블록 찾기
def search(board, idx):
    global max_block
    if idx == 5:
        max_block = max(max_block, max(map(max, board)))  # 현재 보드에서 최대 블록 찾기
        return

    search(up(deepcopy(board)), idx + 1)
    search(down(deepcopy(board)), idx + 1)
    search(left(deepcopy(board)), idx + 1)
    search(right(deepcopy(board)), idx + 1)

max_block = 0
search(board, 0)
print(max_block)

# def up(new_board):
#     max_block = 0
#     save = [[] for _ in range(n)]
#     # 땡기기 
#     for i in range(n):
#         for j in range(n):
#             if new_board[i][j] != 0:
#                 save[j].append(new_board[i][j])
#     for i in range(n):
#         for j in range(n):
#             if len(save[j]) > i:
#                 new_board[i][j] = save[j][i]
#             else:
#                 new_board[i][j] = 0

#     for i in range(n-1): # 0에서 n-2까지
#         for j in range(n): # 가로는 상관없음 0에서 n-1
#             if new_board[i][j] == new_board[i+1][j]:
#                 max_block = max(max_block, new_board[i][j] * 2)
#                 if 0<= i-1 and new_board[i-1][j] == 0:
#                     new_board[i-1][j] = new_board[i][j] * 2
#                     new_board[i+1][j] = new_board[i][j] = 0
#                 else:
#                     new_board[i][j] = new_board[i][j] * 2
#                     new_board[i+1][j] = 0
#             else:
#                 if 0<= i-1 and new_board[i-1][j] == 0:
#                     new_board[i-1][j] = new_board[i][j]
#                     new_board[i][j] = 0
    
#     return max_block, new_board

# def down(new_board):
#     max_block = 0
#     save = [[] for _ in range(n)]
#     for i in range(n):
#         for j in range(n):
#             if new_board[-(i-n-1)][j] != 0:
#                 save[j].append(new_board[-(i-n-1)][j])
#     for i in range(n):
#         for j in range(n):
#             if len(save[j]) > i:
#                 new_board[-(i-n-1)][j] = save[j][i]
#             else:
#                 new_board[-(i-n-1)][j] = 0

#     for i in range(n-1): # n-1에서 1까지
#         for j in range(n): # 가로는 상관없음 0에서 n-1
#             if new_board[-(i-n-1)][j] == new_board[-(i-n-1)-1][j]:
#                 max_block = max(max_block, new_board[-(i-n-1)][j] * 2)
#                 if -(i-n-1)+1 < n and new_board[-(i-n-1)+1][j] == 0:
#                     new_board[-(i-n-1)+1][j] = new_board[-(i-n-1)][j] * 2
#                     new_board[-(i-n-1)-1][j] = new_board[-(i-n-1)][j] = 0
#                 else:
#                     new_board[-(i-n-1)][j] = new_board[-(i-n-1)][j] * 2
#                     new_board[-(i-n-1)-1][j] = 0
#             else:
#                 if -(i-n-1)+1 < n and new_board[-(i-n-1)+1][j] == 0:
#                     new_board[-(i-n-1)+1][j] = new_board[-(i-n-1)][j]
#                     new_board[-(i-n-1)][j] = 0
#     return max_block, new_board

# def left(new_board):
#     max_block = 0
#     save = [[] for _ in range(n)]
#     for i in range(n):
#         for j in range(n):
#             if new_board[i][j] != 0:
#                 save[i].append(new_board[i][j])
#     for i in range(n):
#         for j in range(n):
#             if len(save[i]) > j:
#                 new_board[i][j] = save[i][j]
#             else:
#                 new_board[i][j] = 0
    
#     for i in range(n): # 0에서 n-1
#         for j in range(n-1): # 0에서 n-2, n-1부터
#             if new_board[i][j] == new_board[i][j+1]:
#                 max_block = max(max_block, new_board[i][j] * 2)
#                 if 0<=j-1 and new_board[i][j-1] == 0:
#                     new_board[i][j-1] = new_board[i][j] * 2
#                     new_board[i][j+1] = new_board[i][j] = 0
#                 else:
#                     new_board[i][j] = new_board[i][j] * 2
#                     new_board[i][j+1] = 0   
#             else:
#                 if 0<=j-1 and new_board[i][j-1] == 0:
#                     new_board[i][j-1] = new_board[i][j]
#                     new_board[i][j] = 0

#     return max_block, new_board

# def right(new_board):
#     max_block = 0
#     save = [[] for _ in range(n)]
#     for i in range(n):
#         for j in range(n):
#             if new_board[i][-(j-n-1)] != 0:
#                 save[i].append(new_board[i][-(j-n-1)])
#     for i in range(n):
#         for j in range(n):
#             if len(save[i]) > j:
#                 new_board[i][-(j-n-1)] = save[i][j]
#             else:
#                 new_board[i][-(j-n-1)] = 0

#     for i in range(n): # 0에서 n-1
#         for j in range(n-1): # 0에서 n-2, n-1부터
#             if new_board[i][-(j-n-1)] == new_board[i][-(j-n-1)-1]:
#                 max_block = max(max_block, new_board[i][-(j-n-1)] * 2)
#                 if -(j-n-1)+1 < n and new_board[i][-(j-n-1)+1] == 0:
#                     new_board[i][-(j-n-1)+1] = new_board[i][-(j-n-1)] * 2
#                     new_board[i][-(j-n-1)-1] = new_board[i][-(j-n-1)] = 0
#                 else:
#                     new_board[i][-(j-n-1)] = new_board[i][-(j-n-1)] * 2
#                     new_board[i][-(j-n-1)-1] = 0  
#             else:
#                 if -(j-n-1)+1 < n and new_board[i][-(j-n-1)+1] == 0:
#                     new_board[i][-(j-n-1)+1] = new_board[i][-(j-n-1)]
#                     new_board[i][-(j-n-1)] = 0
#     return max_block, new_board

# def search(board, idx):
#     global max_block
#     if idx > 5:
#         return
#     new_board = deepcopy(board)

#     c, b = up(new_board)
#     max_block = max(max_block, c)
#     search(b, idx + 1)

#     c, b = down(new_board)
#     max_block = max(max_block, c)
#     search(b, idx + 1)

#     c, b = right(new_board)
#     max_block = max(max_block, c)
#     search(b, idx + 1)

#     c, b = left(new_board)
#     max_block = max(max_block, c)
#     search(b, idx + 1)

# max_block = 0
# search(board, 0)
# print(max_block)

