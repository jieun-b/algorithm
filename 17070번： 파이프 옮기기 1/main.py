#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 17070                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: jieunb_b <boj.kr/u/jieunb_b>                +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/17070                          #+#        #+#      #+#     #
#    Solved: 2024/08/27 23:07:53 by jieunb_b      ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
input = sys.stdin.readline

N = int(input())
grid = []
for _ in range(N):
    grid.append(list(map(int, input().split())))

def search(start,end):
    global count
    if end == (N,N):
        count += 1
    if start[0] == end[0]: # 가로
        if end[1]+1 <= N and grid[end[0]-1][end[1]] == 0: # 오른쪽
            search((start[0],start[1]+1),(end[0],end[1]+1))
        if end[1]+1 <= N and end[0]+1 <= N and grid[end[0]-1][end[1]] == 0 and grid[end[0]][end[1]] == 0 and grid[end[0]][end[1]-1] == 0: # 오른쪽 아래
            search((start[0],start[1]+1),(end[0]+1,end[1]+1))
    elif start[1] == end[1]: # 세로
        if end[0]+1 <= N and grid[end[0]][end[1]-1] == 0: # 아래
            search((start[0]+1,start[1]),(end[0]+1,end[1]))
        if end[1]+1 <= N and end[0]+1 <= N and grid[end[0]-1][end[1]] == 0 and grid[end[0]][end[1]] == 0 and grid[end[0]][end[1]-1] == 0: # 오른쪽 아래
            search((start[0]+1,start[1]),(end[0]+1,end[1]+1))
    else: # 대각선
        if end[1]+1 <= N and grid[end[0]-1][end[1]] == 0: # 오른쪽
            search((start[0]+1,start[1]+1),(end[0],end[1]+1))
        if end[0]+1 <= N and grid[end[0]][end[1]-1] == 0: # 아래
            search((start[0]+1,start[1]+1),(end[0]+1,end[1]))
        if end[1]+1 <= N and end[0]+1 <= N and grid[end[0]-1][end[1]] == 0 and grid[end[0]][end[1]] == 0 and grid[end[0]][end[1]-1] == 0: # 오른쪽 아래
            search((start[0]+1,start[1]+1),(end[0]+1,end[1]+1))

count = 0
search((1,1),(1,2))
print(count)
