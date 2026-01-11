#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 3758                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: jieunb_b <boj.kr/u/jieunb_b>                +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/3758                           #+#        #+#      #+#     #
#    Solved: 2025/04/11 18:11:27 by jieunb_b      ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
input = sys.stdin.readline
testcase = int(input())
for _ in range(testcase):
    n, k, t, m = map(int, input().split())
    logs = [list(map(int, input().split())) for _ in range(m)]
    board = [[0]*k for _ in range(n)]
    submit = [0 for _ in range(n)]
    time = [0 for _ in range(n)]
    for i in range(m):
        board[logs[i][0]-1][logs[i][1]-1] = max(board[logs[i][0]-1][logs[i][1]-1], logs[i][2])
        submit[logs[i][0]-1] += 1
        time[logs[i][0]-1] = i
    infos = []
    for i in range(n):
        infos.append([i+1, sum(board[i]), submit[i], time[i]])
    infos = sorted(infos, key=lambda x: (-x[1], x[2], x[3]))
    
    rank = 0
    for info in infos:
        rank += 1
        if info[0] == t:
            break
    print(rank)