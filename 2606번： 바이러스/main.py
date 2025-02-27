#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 2606                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: jieunb_b <boj.kr/u/jieunb_b>                +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/2606                           #+#        #+#      #+#     #
#    Solved: 2025/02/13 00:30:14 by jieunb_b      ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
input = sys.stdin.readline

num = int(input())
pair = int(input())

computers = [[] for _ in range(num+1)]
visited = [False for _ in range(num+1)]

for _ in range(pair):
    c1, c2 = map(int, input().split())
    computers[c1].append(c2)
    computers[c2].append(c1)

def search(c, count):
    visited[c] = True  
    for computer in computers[c]:
        if not visited[computer]: 
            count = search(computer, count + 1) 
    return count

count = search(1, 0) 
print(count)