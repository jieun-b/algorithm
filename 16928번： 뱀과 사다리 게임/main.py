#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 16928                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: jieunb_b <boj.kr/u/jieunb_b>                +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/16928                          #+#        #+#      #+#     #
#    Solved: 2025/03/05 16:16:26 by jieunb_b      ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int,input().split())
visited = [0]*101
ladder = {}
snake = {}

for _ in range(n):
    x, y = map(int, input().split())
    ladder[x] = y
for _ in range(m):
    u, v = map(int, input().split())
    snake[u] = v

# 숫자가 주어졌을 때 i, j는 i=(num // 10)-1  j=(num%10)-1
# [0,0]에서 선택할 수 있는 주사위는 1~6
# 각 번호에 따라 선택할 수 있는 수 -> 6^k 

def search():
    queue = deque([(1, 0)]) # 현재 위치(인덱스), 주사위 횟수 
    visited[1] = 1
    while queue:
        idx, depth = queue.popleft() 
        if idx == 100:
            return depth
        for i in range(1, 7):
            next_idx = idx+i
            if next_idx > 100:
                continue
            while next_idx in ladder or next_idx in snake:
                if next_idx in ladder:
                    next_idx = ladder[next_idx]
                if next_idx in snake:
                    next_idx = snake[next_idx]
            if visited[next_idx] == 0:
                visited[next_idx] = 1
                queue.append((next_idx, depth+1))

print(search())
