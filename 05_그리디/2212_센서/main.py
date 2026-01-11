#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 2212                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: jieunb_b <boj.kr/u/jieunb_b>                +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/2212                           #+#        #+#      #+#     #
#    Solved: 2025/07/29 22:51:29 by jieunb_b      ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
input = sys.stdin.readline

n = int(input())
k = int(input())
pos = list(map(int, input().split()))
pos.sort()

dis = [0]*(n-1)
for i in range(n-1):
    dis[i] = pos[i+1]-pos[i]

dis.sort(reverse=True)
print(sum(dis[k-1:]))
# 집중국 사이 거리 합 구하기
# k = 2
# 1 6 9 3 6 7
# 1 3 6 6 7 9
#  2 3 0 1 2
# - i - - i -

# 20 3 14 6 7 8 18 10 12 15
# 3 6 7 8 10 12 14 15 18 20
# - i - -  - -  -  -   i  -
#  3 1 1 2  2  2  1  3  2
# 3+3+2+2+2=12