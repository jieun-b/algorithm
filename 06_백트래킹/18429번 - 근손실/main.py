#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 18429                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: jieunb_b <boj.kr/u/jieunb_b>                +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/18429                          #+#        #+#      #+#     #
#    Solved: 2025/10/11 22:08:42 by jieunb_b      ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
a = list(map(int, input().split()))
visted = [False] * n

# n일동안 순서 조합
# 선택하지 않은 것 선택 만약 조건에 어긋나면 나가기
# visited 만들기 -> 선택한 경우 true로, day는 기록

def search(num, weight): # 지금까지의 운동 키트 수, 현재 중량
    global res
    if weight < 500: # 조건을 만족하지 않으면 종료
        return
    if num == n: 
        res += 1
        return
    for i in range(n): # 전체 돌면서 선택하지 않은 키트 찾기
        if not visted[i]:
            visted[i] = True
            search(num+1, weight-k+a[i]) 
            visted[i] = False

res = 0
search(0, 500)
print(res)