#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 15681                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: jieunb_b <boj.kr/u/jieunb_b>                +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/15681                          #+#        #+#      #+#     #
#    Solved: 2025/08/01 21:29:53 by jieunb_b      ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
from collections import deque
input = sys.stdin.readline

n, r, q = map(int, input().split())
connect = [[] for _ in range(n+1)]
tree = [[-1,[]] for _ in range(n+1)]
size = [0 for _ in range(n+1)]
for _ in range(n-1):
    a, b = map(int, input().split())
    connect[a].append(b)
    connect[b].append(a)

def makeTree(currentNode, parent):
    queue = deque([(currentNode, parent)])
    while(queue):
        currentNode, parent = queue.popleft()
        stack.append(currentNode)
        for node in connect[currentNode]:
            if parent == -1 or node != parent:
                tree[currentNode][1].append(node)
                tree[node][0] = currentNode
                queue.append((node, currentNode))

stack = []
makeTree(r, -1)
while stack:
    node = stack.pop()
    size[node] += 1
    if node != r:
        size[tree[node][0]] += size[node]
for _ in range(q):
    u = int(input())
    print(size[u])