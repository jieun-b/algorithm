#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 12919                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: jieunb_b <boj.kr/u/jieunb_b>                +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/12919                          #+#        #+#      #+#     #
#    Solved: 2025/05/24 17:28:31 by jieunb_b      ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
from collections import deque
input = sys.stdin.readline

s = list(input().strip())
t = list(input().strip())

def bfs(t):
    queue = deque([t])
    while(queue):
        word = queue.popleft()
        if word == s:
            return 1
        if word[-1] == 'A' and len(word) > 1:
            queue.append(word[:len(word)-1])
        tmp = list(reversed(word))
        if tmp[-1] == 'B' and len(word) > 1:
            queue.append(tmp[:len(word)-1])
    return 0

print(bfs(t))