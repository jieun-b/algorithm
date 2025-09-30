#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 1449                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: jieunb_b <boj.kr/u/jieunb_b>                +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/1449                           #+#        #+#      #+#     #
#    Solved: 2025/09/23 16:42:06 by jieunb_b      ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
input = sys.stdin.readline

n, l = map(int, input().split())
pos = list(map(int, input().split()))
pos.sort()

# 테이프 개수 = count
# 현재 테이프 시작점 = idx 
# 위치를 순서대로 탐색하면서
    # 현재 위치에서 pos[idx]의 값 빼기 + 1이 l보다 작거나 같으면 커버
    # 크면 idx는 현재 위치, count+1  

count = 1
idx = 0
for i in range(1, n):
    cover = pos[i] - pos[idx] + 1
    if cover > l:
        idx = i
        count += 1
print(count)