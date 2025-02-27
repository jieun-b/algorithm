#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 14500                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: jieunb_b <boj.kr/u/jieunb_b>                +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/14500                          #+#        #+#      #+#     #
#    Solved: 2025/02/26 13:27:49 by jieunb_b      ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
# import sys
# input = sys.stdin.readline

# n, m = map(int, input().split())
# paper = [list(map(int, input().split())) for _ in range(n)]

# # 1번 -> 2가지 경우의 수
# # 2번 -> 1가지 경우의 수
# # 3번 -> 8가지 경우의 수
# # 4번 -> 4가지 경우의 수
# # 5번 -> 4가지 경우의 수
# # 500x500x20 = 5,000,000

# all_case = [[(0,1),(0,2),(0,3)],[(1,0),(2,0),(3,0)],
#             [(0,1),(1,1),(1,0)],
#             [(1,0),(2,0),(2,1)],[(1,0),(2,0),(2,-1)],[(1,0),(1,1),(1,2)],[(0,1),(0,2),(1,0)],
#             [(0,1),(1,0),(2,0)],[(0,1),(1,1),(2,1)],[(1,0),(1,-1),(1,-2)],[(0,1),(0,2),(1,2)],
#             [(1,0),(1,1),(2,1)],[(1,0),(1,-1),(2,-1)],[(0,1),(1,1),(1,2)],[(0,-1),(1,-1),(1,-2)],
#             [(0,1),(0,2),(1,1)],[(0,1),(0,2),(-1,1)],[(1,0),(2,0),(1,-1)],[(1,0),(2,0),(1,1)]]

# def check(i, j, k):
#     current_sum = paper[i][j]
#     for dir in all_case[k]:
#         if 0<=i+dir[0]<n and 0<=j+dir[1]<m:
#             current_sum += paper[i+dir[0]][j+dir[1]]
#         else:
#             return 0
#     return current_sum
                
# max_num = 0
# # 종이 한 칸마다 전체 케이스 실행해보기 
# for i in range(n):
#     for j in range(m):
#         # 특정 칸에서 모든 케이스 실행
#         for k in range(len(all_case)):
#             # 특정 칸에서 특정 테트로미노 확인
#             max_num = max(max_num, check(i, j, k))

# print(max_num)

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
paper = [list(map(int, input().split())) for _ in range(n)]
visited = [[False]*m for _ in range(n)]

except_case = [[(0,1),(0,2),(1,1)],[(0,1),(0,2),(-1,1)],[(1,0),(2,0),(1,-1)],[(1,0),(2,0),(1,1)]]

# ㅜ 모양을 제외하면 dfs로 모든 탐색을 하는거랑 같아짐
dx = [1,0,-1,0]
dy = [0,1,0,-1]

def check(i, j, k):
    current_sum = paper[i][j]
    for dir in except_case[k]:
        if 0<=i+dir[0]<n and 0<=j+dir[1]<m:
            current_sum += paper[i+dir[0]][j+dir[1]]
        else:
            return 0
    return current_sum

def search(idx, i, j, current_sum):
    # 만약 현재 인덱스가 4이면 종료
    # 현재 값이 종이에서 젤 큰 숫자*? 보다 크면 굳이 확인안해도 됨
    global max_sum
    if idx == 4:
        max_sum = max(max_sum, current_sum)
        return 
    if max_sum >= current_sum + max_paper*(4-idx):
        return
    # 현재 인덱스에서 전진
    for k in range(4):
        y = i + dy[k]
        x = j + dx[k]
        if 0<=y<n and 0<=x<m and not visited[y][x]:
            visited[y][x] = True
            search(idx+1, y, x, current_sum+paper[y][x])
            visited[y][x] = False

# max_paper = 0
# for p in paper:
#     max_tmp = max(p)
#     max_paper = max(max_tmp)
max_paper = max(max(p) for p in paper)

max_sum = 0
for i in range(n):
    for j in range(m):
        visited[i][j] = True
        search(1, i, j, paper[i][j])        
        visited[i][j] = False
        for k in range(4):
            max_sum = max(max_sum, check(i, j, k))

print(max_sum)

