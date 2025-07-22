#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 15686                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: jieunb_b <boj.kr/u/jieunb_b>                +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/15686                          #+#        #+#      #+#     #
#    Solved: 2025/07/21 23:12:23 by jieunb_b      ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
city = [list(map(int, input().split())) for _ in range(n)]

house = []
chicken = []
for i in range(n):
    for j in range(n):
        if city[i][j] == 1:
            house.append((i+1, j+1))
        elif city[i][j] == 2:
            chicken.append((i+1, j+1))
# 모든 집마다 모든 치킨집 사이 거리 구하기: 2n*13 -> 위치 정하기 애매함
# 치킨집은 최대 13개 13개를 선택하는 경우의 수 찾기
dis = []  
for i in range(len(chicken)):
    tmp = []
    for j in range(len(house)):
        tmp.append(abs(chicken[i][0]-house[j][0])+abs(chicken[i][1]-house[j][1]))
    dis.append(tmp)


def search(idx, depth, matrix):
    global min_dis
    if len(chicken[idx+1:]) < m-depth:
        return
    if depth == m:
        count = 0
        for j in range(len(house)):
            tmp = float('inf')
            for i in range(len(matrix)):
                tmp = min(tmp, matrix[i][j])
            count += tmp
        min_dis = min(min_dis, count)
        return
    for i in range(idx+1, len(chicken)):
        matrix.append(dis[i])
        search(i, depth+1, matrix)
        matrix.pop()

min_dis = float('inf')
search(-1, 0, [])
print(min_dis)