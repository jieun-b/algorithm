#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 9663                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: jieunb_b <boj.kr/u/jieunb_b>                +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/9663                           #+#        #+#      #+#     #
#    Solved: 2024/06/04 23:06:18 by jieunb_b      ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

N = int(input())

cnt = 0
p = []

def dfs(i,j):
    global cnt
    if len(p) == N:
        cnt += 1
        return
    for n in range(i,N):
        for m in range(N):
            if n == i and m <= j: continue
            flag = 1
            for k in p:
                if n == k[0] or m == k[1] or abs(n-k[0]) == abs(m-k[1]): flag = 0
            if flag:
                p.append((n,m))
                dfs(n,m)
                p.pop() 

for i in range(N):
    for j in range(N):
        p.append((i,j))
        dfs(i,j)
        p.pop()

print(cnt)
