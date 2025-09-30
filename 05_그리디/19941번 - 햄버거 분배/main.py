#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 19941                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: jieunb_b <boj.kr/u/jieunb_b>                +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/19941                          #+#        #+#      #+#     #
#    Solved: 2025/04/09 22:20:09 by jieunb_b      ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
pos = list(input().strip())
visited = [0]*n

for i in range(n):
    if pos[i] == "H":
        for j in range(-k, k+1):
            if 0<=i+j<n and pos[i+j] == "P" and visited[i+j] == 0:
                visited[i+j] = 1
                break

print(visited.count(1))