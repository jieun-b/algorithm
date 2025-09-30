#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 6987                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: jieunb_b <boj.kr/u/jieunb_b>                +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/6987                           #+#        #+#      #+#     #
#    Solved: 2024/06/10 16:29:44 by jieunb_b      ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys

input = sys.stdin.readline

def dfs(i, j):
    global ans
    if j == 6:
        i = i+1
        j = i+1
    if i == 5:
        if info == [0 for _ in range(18)]:
            ans = 1
        return
    
    for k in range(3): # 0이면 i가 이김, 1이면 비김, 2이면 j가 이김
        if info[i*3+k]>0 and info[j*3+(2-k)]>0:
            info[i*3+k] -= 1
            info[j*3+(2-k)] -= 1
            dfs(i,j+1)
            info[i*3+k] += 1
            info[j*3+(2-k)] += 1

res = []
for _ in range(4):
    info = list(map(int, input().split()))
    ans = 0
    dfs(0,1)
    res.append(ans)

print(*res)