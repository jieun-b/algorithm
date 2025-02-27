#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 2667                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: jieunb_b <boj.kr/u/jieunb_b>                +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/2667                           #+#        #+#      #+#     #
#    Solved: 2025/02/11 20:51:46 by jieunb_b      ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
graph = []
visited = []
# 입력이 연속적인 숫자일 때
# 하나씩 잘라서 리스트에 넣는 방법
# 문자열로 입력받아 바로 리스트로 바꾸면 됨
# strip은 양쪽 공백, 줄바꿈 제거

for i in range(n):
    graph.append(list(str(input()).strip()))
    visited.append([False for _ in range(len(graph[i]))])

# bfs 문제인듯
# 첫칸부터 돌면서 1이면 주위를 계속 탐색
# visit 정의하고 방문했으면 더 안가는걸로
# 방문했음 -1로 설정하는걸로
# 단지 한번 끝나면 count 올리기

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def search(i, j):
    # deque()에 원소를 넣을 때는 리스트로 묶어서 넣음
    queue = deque([(i, j)])
    visited[i][j] = True
    count = 1
    while queue:
        y, x = queue.popleft()
        for k in range(4):
            new_y = y + dy[k]
            new_x = x + dx[k]
            if 0<=new_y<len(graph) and 0<=new_x<len(graph[0]):
                if not visited[new_y][new_x] and graph[new_y][new_x] == "1": 
                    count += 1
                    queue.append((new_y, new_x))
                visited[new_y][new_x] = True
    houses.append(count)

houses = []
# 전체 돌면서 확인
for i in range(len(visited)):
    for j in range(len(visited[0])):
        # 방문 안했고 집이 있으면 탐색
        if not visited[i][j] and graph[i][j] == '1': 
            search(i, j)
        visited[i][j] = True

print(len(houses))
for h in sorted(houses):
    print(h)