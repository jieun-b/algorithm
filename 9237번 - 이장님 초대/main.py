#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 9237                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: jieunb_b <boj.kr/u/jieunb_b>                +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/9237                           #+#        #+#      #+#     #
#    Solved: 2025/09/07 14:12:12 by jieunb_b      ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
input = sys.stdin.readline

n = int(input())
t = list(map(int, input().split()))

# 가장 긴 시간이 걸리는 나무를 먼저 심기 / 그리디는 배수 혹은 앞의 사건이 뒤에도 영향을 줄 때
t.sort(reverse=True)

# day = 0
# for tree in t:
#     if tree >= day:
#        day = tree - 1
#     else:
#        day -= 1
# print(len(t)+day+2)

t.sort(reverse=True)   # 긴 시간 먼저
res = 0
for i in range(n):
    res = max(res, i + 1 + t[i])  # i+1일째 심은 나무의 완전 성장일
print(res + 1)  # 다음 날 이장님 초대

# 정렬: t = [4, 3, 3, 2]
# 각 나무 계산:
# 1번째 날 심은 나무(4일): 1+4 = 5일째 완성
# 2번째 날 심은 나무(3일): 2+3 = 5일째 완성
# 3번째 날 심은 나무(3일): 3+3 = 6일째 완성
# 4번째 날 심은 나무(2일): 4+2 = 6일째 완성

# 최댓값 = 6

# +1 (다음 날) = 7 → 정답.