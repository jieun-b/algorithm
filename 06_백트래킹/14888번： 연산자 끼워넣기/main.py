#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 14888                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: jieunb_b <boj.kr/u/jieunb_b>                +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/14888                          #+#        #+#      #+#     #
#    Solved: 2025/02/18 02:50:36 by jieunb_b      ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
input = sys.stdin.readline

n = int(input())
a_n = list(map(int, input().split()))
symbols = list(map(int, input().split()))

# a_n의 값들은 고정, symbols에서 하나씩 빼기

# 조건 함수
def operate(result, current, idx):
    if idx == 0:
        result = result+a_n[current]
    elif idx == 1:
        result = result-a_n[current]
    elif idx == 2:
        result = result*a_n[current]
    else:
        if result < 0:
            result = -(abs(result)//a_n[current])
        else:
            result = result//a_n[current]
    return result

# 탐색 함수
def search(result, current):
    # 종료 조건
    if current == n:
        results.append(result)
        return
    # +,-,*,% 중에 하나 선택
    for idx in range(4):
        # 해당 연산자를 사용할 수 있으면 계산
        if symbols[idx] != 0:
            symbols[idx] -= 1
            search(operate(result, current, idx), current+1)
            symbols[idx] += 1

results = []
search(a_n[0], 1)
results.sort()
print(results[-1])
print(results[0])