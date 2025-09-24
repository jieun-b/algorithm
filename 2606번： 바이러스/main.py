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



import sys
from collections import deque
input = sys.stdin.readline

# 그래프 문제 - 특정 노드와 연결되는 모든 노드 찾기
n = int(input())
edge = int(input())
linked = [[] for _ in range(n+1)]
for _ in range(edge):
    a, b = map(int, input().split())
    linked[a].append(b)
    linked[b].append(a)

def search(num):
    queue = deque([num])
    visited[num] = 1
    while(queue):
        cur_node = queue.popleft()
        for i in range(len(linked[cur_node])):
            next_node = linked[cur_node][i]
            if not visited[next_node]: 
                queue.append(next_node)
                visited[next_node] = 1

visited = [0] * (n+1)
search(1)

print(sum(visited)-1)