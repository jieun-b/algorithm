#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 15683                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: jieunb_b <boj.kr/u/jieunb_b>                +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/15683                          #+#        #+#      #+#     #
#    Solved: 2025/06/18 20:29:58 by jieunb_b      ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
input = sys.stdin.readline

n, m = map(int, input().split())

cctv = []
office = []
for i in range(n):
    row = list(map(int, input().split()))
    office.append(row)
    for j in range(m):
        if row[j] != 0 and row[j] != 6:
            cctv.append((row[j], i, j))
cctv.sort(reverse=True)

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

config = [
    [],
    [[0], [1], [2], [3]],
    [[0,1], [2,3]],
    [[0, 3], [3, 1], [1, 2], [2, 0]],
    [[2, 0, 3], [0, 3, 1], [3, 1, 2], [1, 2, 0]],
    [[0,1,2,3]],
]

def search(cctv_idx):
    global result
    if cctv_idx == len(cctv):
        count = 0
        for row in office:
            for r in row:
                if r == 0:
                    count += 1
        result = min(result, count)
        return
    num, i, j = cctv[cctv_idx]
    changed = []
    # config[num]: cctv 번호에 따라 가능한 조합 (리스트들)
    for idx in range(len(config[num])): # 가능한 조합 수에 따라 반복 -> 택 1
        # config[num][k]: 갈 수 있는 인덱스 (방향 번호)
        for dir in config[num][idx]: # 가능한 방향에 따라 반복 -> dir은 dx, dy의 인덱스 -> 무조건 채워야 됨
            new_i, new_j = i, j
            while(True):
                new_i = new_i + dy[dir]
                new_j = new_j + dx[dir]
                if 0<=new_i<n and 0<=new_j<m:
                    if office[new_i][new_j] == 6:
                        break
                    else:
                        if office[new_i][new_j] == 0:
                            office[new_i][new_j] = -1
                            changed.append((new_i, new_j))
                else:
                    break
        search(cctv_idx+1)
        while changed:
            changed_i, changed_j = changed.pop()
            office[changed_i][changed_j] = 0

result = float('inf')
search(0)
print(result)