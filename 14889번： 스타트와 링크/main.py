#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 14889                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: jieunb_b <boj.kr/u/jieunb_b>                +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/14889                          #+#        #+#      #+#     #
#    Solved: 2025/02/21 01:01:02 by jieunb_b      ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
input = sys.stdin.readline

n = int(input())
s = [list(map(int, input().split())) for _ in range(n)]
visited = [False]*n
min_diff = sys.maxsize

def search(idx, count):
    global min_diff
    if count == n//2:
        a, b = 0, 0
        for i in range(n):
            for j in range(i+1, n):
                if visited[i] and visited[j]:
                    a += s[i][j] + s[j][i]
                if not visited[i] and not visited[j]:
                    b += s[i][j] + s[j][i]
        diff = abs(a - b)
        min_diff = min(min_diff, diff)
        return
    if (n//2-count) + idx < n//2:
        return
    for i in range(idx, n):
        if not visited[i]:
            visited[i] = True
            search(i+1, count+1)
            visited[i] = False

search(0, 0)
print(min_diff)