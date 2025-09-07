#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 9372                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: jieunb_b <boj.kr/u/jieunb_b>                +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/9372                           #+#        #+#      #+#     #
#    Solved: 2025/09/07 14:59:49 by jieunb_b      ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
input = sys.stdin.readline

def search(country):
    global count
    for i in range(len(connect[country])):
        if not visited[connect[country][i]]:
            visited[connect[country][i]] = True
            count += 1
            search(connect[country][i])

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    connect = [[] for _ in range(n+1)]
    for _ in range(m):
        a, b = map(int, input().split())
        connect[a].append(b)
        connect[b].append(a)
    visited = [False] * (n+1)
    visited[1] = True
    count = 0
    search(1)
    print(count)


# t = int(input())
# for _ in range(t):
#     n, m = map(int, input().split())
#     for _ in range(m):
#         input() 
#     print(n-1)