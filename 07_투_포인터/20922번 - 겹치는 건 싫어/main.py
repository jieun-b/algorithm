#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 20922                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: jieunb_b <boj.kr/u/jieunb_b>                +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/20922                          #+#        #+#      #+#     #
#    Solved: 2025/04/24 22:05:21 by jieunb_b      ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
a_n = list(map(int, input().split()))

# 연속된 길이를 찾으려면 처음부터 끝까지 봐야함 o(n)
# 투 포인터로 풀기
left, count = 0, 0
compare = dict()
for i in range(n):
    if a_n[i] not in compare:
        compare[a_n[i]] = 1
    else:
        compare[a_n[i]] += 1
    while compare[a_n[i]] > k:
        compare[a_n[left]] -= 1
        left += 1
    count = max(count, i-left)
print(count+1)