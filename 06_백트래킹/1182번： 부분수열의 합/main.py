#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 1182                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: jieunb_b <boj.kr/u/jieunb_b>                +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/1182                           #+#        #+#      #+#     #
#    Solved: 2024/06/10 15:45:29 by jieunb_b      ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
input = sys.stdin.readline

n, s = map(int, input().split())
integer = list(map(int, input().split()))

def search(idx, s):
    global count
    if sum(sub) == s:
        count += 1
    for i in range(idx, n):
        sub.append(integer[i])
        search(i+1, s)
        sub.pop()

sub = []
count = 0
search(0, s)
print(count)

# import sys

# input = sys.stdin.readline
# N, S = map(int, input().split())
# num = list(map(int, input().split()))

# res = 0
# def dfs(idx):
#     global res            
#     for i in range(idx, N):
#         sub.append(num[i]) 
#         if sum(sub) == S:
#             res += 1  
#         dfs(i+1)
#         sub.pop()

# sub = []
# dfs(0)

# print(res)