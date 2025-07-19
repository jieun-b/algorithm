#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 21608                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: jieunb_b <boj.kr/u/jieunb_b>                +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/21608                          #+#        #+#      #+#     #
#    Solved: 2025/07/19 23:26:12 by jieunb_b      ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
input = sys.stdin.readline

n = int(input())
info = [list(map(int, input().split())) for _ in range(n**2)]

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

grid = [[0]*n for _ in range(n)]
for student in info:
    find = []
    for i in range(n):
        for j in range(n):
            if grid[i][j] != 0:
                continue
            close = 0
            empty = 0
            for k in range(4):
                new_i = di[k] + i
                new_j = dj[k] + j
                if 0<=new_i<n and 0<=new_j<n:
                    if grid[new_i][new_j] == 0:
                        empty += 1
                    elif grid[new_i][new_j] in student[1:]:
                        close += 1
            find.append([close, empty, i, j])    
    find.sort(key=lambda x: (-x[0], -x[1], x[2], x[3]))
    select = find[0]
    grid[select[2]][select[3]] = student[0]

info.sort()
result = 0
for i in range(n):
    for j in range(n):
        students = info[grid[i][j]-1][1:]
        count = 0
        for k in range(4):
            new_i = di[k] + i
            new_j = dj[k] + j
            if 0<=new_i<n and 0<=new_j<n:
                if grid[new_i][new_j] in students:
                    count += 1
        if count != 0:
            result += 10**(count-1)
print(result)