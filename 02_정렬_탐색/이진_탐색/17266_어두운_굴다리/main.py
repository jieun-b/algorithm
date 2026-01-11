#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 17266                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: jieunb_b <boj.kr/u/jieunb_b>                +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/17266                          #+#        #+#      #+#     #
#    Solved: 2025/04/05 18:02:52 by jieunb_b      ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
input = sys.stdin.readline

n = int(input())  # 길이
m = int(input())  # 조명 수
x = list(map(int, input().split()))  # 조명 위치 (오름차순 정렬되어 있음이 보장되었는지 확인 필요)

def check(height):
    # 현재 높이로 모든 구간이 커버되는지 확인
    current = 0  # 현재 커버된 마지막 위치
    for pos in x:
        left = pos - height
        right = pos + height
        if left > current:
            return False
        current = max(current, right)
    return current >= n  # 마지막까지 커버했는지 확인

# 이진 탐색
low = 0
high = n
result = n
while low <= high:
    mid = (low + high) // 2
    if check(mid):
        result = mid
        high = mid - 1
    else:
        low = mid + 1

print(result)