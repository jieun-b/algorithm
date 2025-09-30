#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 17484                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: jieunb_b <boj.kr/u/jieunb_b>                +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/17484                          #+#        #+#      #+#     #
#    Solved: 2025/04/11 01:31:37 by jieunb_b      ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]

def search(i, j, d, s):
    global fuel
    s += matrix[i][j]
    if fuel <= s:
        return
    if i == n-1:
        fuel = min(fuel, s)
        return
    for k in range(-1, 2):
        if d is not None and d == k: 
            continue
        if 0<=j+k<m: 
            search(i+1, j+k, k, s)
    
fuel = float('inf')
for k in range(m):
    search(0, k, None, 0)
print(fuel)