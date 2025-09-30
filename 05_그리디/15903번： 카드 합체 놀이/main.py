#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 15903                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: jieunb_b <boj.kr/u/jieunb_b>                +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/15903                          #+#        #+#      #+#     #
#    Solved: 2024/09/25 20:18:51 by jieunb_b      ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
states = list(map(int, input().split()))

# 매번 가장 작은 수를 가진 카드를 골라 더함
for _ in range(m):
    states = sorted(states)
    new_state = states[0] + states[1]
    states[0] = new_state
    states[1] = new_state

print(sum(states))