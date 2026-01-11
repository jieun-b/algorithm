#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 1759                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: jieunb_b <boj.kr/u/jieunb_b>                +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/1759                           #+#        #+#      #+#     #
#    Solved: 2024/06/10 16:29:05 by jieunb_b      ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
input = sys.stdin.readline

L,C = map(int, input().split()) # L: 최소 한 개 모음 + 최소 두 개 자음
c = sorted(list(map(str, input().split())))
m = ['a', 'e', 'i', 'o', 'u']
one = 0
two = 0

def dfs(idx):
    global one
    global two
    if len(res) == L:
        print(''.join(res))
        return
    for i in range(idx, C): 
        if c[i] in m: # 모음일 때
            if (L-len(res) == 1 and two == 1) or (L-len(res) == 2 and two == 0):
                continue
            else: 
                one += 1 
                res.append(c[i])
                dfs(i+1)
                res.pop()
                one -= 1
        else:  # 자음일 때 
            if L-len(res) == 1 and one == 0: 
                continue
            else:
                two += 1
                res.append(c[i])
                dfs(i+1)
                res.pop()
                two -= 1

res = []
dfs(0)
