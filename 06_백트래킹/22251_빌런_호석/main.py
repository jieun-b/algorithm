#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 22251                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: jieunb_b <boj.kr/u/jieunb_b>                +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/22251                          #+#        #+#      #+#     #
#    Solved: 2025/05/28 20:49:50 by jieunb_b      ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
input = sys.stdin.readline

n, k, p, x = map(int, input().split())
light = [
            '1111101', # 0
            '0011000', # 1
            '0110111', # 2
            '0011111', # 3
            '1011010', # 4
            '1001111', # 5
            '1101111', # 6
            '0011100', # 7
            '1111111', # 8
            '1011111', # 9
        ]

display = [0] * k
for i in range(k):
    display[k-i-1] = x % 10
    x = x // 10
original = ''.join(map(str, display))

sub = [[0]*10 for _ in range(10)]
for i in range(10):
    for j in range(10):
        int_i = int(light[i],2)
        int_j = int(light[j],2)
        diff = bin(int_i^int_j).count('1')
        sub[i][j] = diff

def search(pos, rev, combi): # 조합하는 자리, 반전 횟수, 문자열
    global ans
    # 반전 횟수 초과
    if rev > p:
        return
    # 종료 조건
    if pos == k:
        # 범위 안에 들때 
        if 1 <= int(combi) <= n and combi != original:
            ans += 1
            return
        # 범위 안에 안들면
        else:
            return
    for i in range(10):
        if display[pos] != i:
            search(pos+1, rev+sub[display[pos]][i], combi+str(i))
        else:
            search(pos+1, rev, combi+str(i))

ans = 0
search(0, 0, '')
print(ans)