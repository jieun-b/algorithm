#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 2816                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: jieunb_b <boj.kr/u/jieunb_b>                +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/2816                           #+#        #+#      #+#     #
#    Solved: 2025/03/09 13:13:09 by jieunb_b      ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
input = sys.stdin.readline

n = int(input())
channels = [input().strip() for _ in range(n)]

find = ['KBS1', 'KBS2']
button = ''

# 탐색하면서 현재 채널 위 아래에 찾는 채널 명이 있는지 확인
# 없다면 문자열에 1 추가
idx_1 = 0
idx_2 = 0
for i in range(len(channels)):
    if channels[i] == find[0]:
        idx_1 = i
    if channels[i] == find[1]:
        idx_2 = i

button += idx_1 * '1'
button += idx_1 * '4'

if idx_1 > idx_2:
    idx_2 += 1
button += idx_2 * '1'
button += (idx_2-1) * '4'

print(button)