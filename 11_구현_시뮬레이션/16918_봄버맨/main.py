#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 16918                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: jieunb_b <boj.kr/u/jieunb_b>                +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/16918                          #+#        #+#      #+#     #
#    Solved: 2025/06/27 23:48:04 by jieunb_b      ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
input = sys.stdin.readline

r, c, n = map(int, input().split())

first = [list(input().strip()) for _ in range(r)]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def explode(grid):
    result = [['O']*c for _ in range(r)]
    for i in range(r):
        for j in range(c):
            if grid[i][j] == 'O':
                result[i][j] = '.'
                for k in range(4):
                    new_i = i+dy[k]
                    new_j = j+dx[k]
                    if 0<=new_i<r and 0<=new_j<c:
                        result[new_i][new_j] = '.'
    return result

if n == 1:
    result = first
elif n % 2 == 0:
    result = [['O']*c for _ in range(r)]
elif n % 4 == 3:
    result = explode(first)
elif n % 4 == 1:
    result = explode(explode(first))

for i in range(r):
    print(''.join(result[i]))