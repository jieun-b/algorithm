#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 14719                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: jieunb_b <boj.kr/u/jieunb_b>                +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/14719                          #+#        #+#      #+#     #
#    Solved: 2024/09/18 19:17:34 by jieunb_b      ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
input = sys.stdin.readline

H, W = map(int,input().split())
graph = [[0]*W for _ in range(H)]

block = list(map(int, input().split()))

for w in range(len(block)):
    for h in range(block[w]):
        graph[-(h+1)][w] = 1

count = 0
for h in range(H):
    flag = False
    tmp = 0
    for w in range(W):
        if graph[h][w] == 1:
            flag = True
            count += tmp
            tmp = 0
        else:
            if flag:
                tmp += 1

print(count)