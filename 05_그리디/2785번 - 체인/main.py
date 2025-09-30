#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 2785                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: jieunb_b <boj.kr/u/jieunb_b>                +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/2785                           #+#        #+#      #+#     #
#    Solved: 2025/07/29 23:41:23 by jieunb_b      ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
input = sys.stdin.readline

n = int(input())
chain = list(map(int, input().split()))
chain.sort()

# 결합한 체인의 개수, 남은 체인의 개수, 사용한 고리의 개수
# used, remain, ring // used = n - remain
# 처음 체인의 수가 남은 체인의 개수보다 작아야 함 for c in chains  c < remain
    # 결합한 체인의 개수 += 체인의 수(c) + 1(고리)
    # 사용한 고리의 개수 = 체인의 수
# 아니라면 사용한 고리의 개수는 남은 체인의 수 -1

used = 1
ring = 0
for c in chain:
    if c < len(chain)-used:
        used += c + 1
        ring += c
    else:
        ring += len(chain)-used
        break
print(ring)