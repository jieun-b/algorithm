#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 2179                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: jieunb_b <boj.kr/u/jieunb_b>                +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/2179                           #+#        #+#      #+#     #
#    Solved: 2025/06/07 13:15:57 by jieunb_b      ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
input = sys.stdin.readline

n = int(input())
words = [(input().strip(), i) for i in range(n)]

words.sort()

max_length = 0
min_idx = float('inf')
prefix = ''
for i in range(n-1):
    a, b = words[i][0], words[i+1][0]
    a_idx, b_idx = words[i][1], words[i+1][1]
    if a == b:
        continue
    
    count = 0
    while(count < len(a) and count < len(b) and a[count] == b[count]):
        count += 1
    if count == 0:
        continue
    
    if max_length < count:
        max_length = count
        prefix = a[:count]
        min_idx = min(a_idx, b_idx)
    elif max_length == count:
        if min_idx > min(a_idx, b_idx):
            min_idx = min(a_idx, b_idx)
            prefix = a[:count]

ans = []
for word, idx in words:
    if word[:len(prefix)] == prefix:
        ans.append((idx, word))

ans.sort(key=lambda x: x[0])
print(ans[0][1])
print(ans[1][1])