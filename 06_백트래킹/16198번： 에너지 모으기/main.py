#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 16198                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: jieunb_b <boj.kr/u/jieunb_b>                +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/16198                          #+#        #+#      #+#     #
#    Solved: 2025/02/28 22:17:00 by jieunb_b      ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
input = sys.stdin.readline
n = int(input())
w_n = list(map(int, input().split()))

# 리스트 인덱싱으로 하면 1
# 모을 수 있는 에너지 양의 최댓값 
# 양 옆에 있는 값이 클수록 최대
# 한 번 구슬을 고를 때마다 최대 8번 최댓값 계산, 전체 8!

def search(current_list, current):
    global total
    if len(current_list) == 2:
        total = max(total, current)
        return
    for i in range(1, len(current_list)-1):
        new_list = current_list[:i]+current_list[i+1:]
        search(new_list, current + current_list[i-1]*current_list[i+1])

total = 0
search(w_n, 0)
print(total)

# 매번 최대에 대해서 하는건 실제로 에너지의 최댓값을 출력하지 않을 수 있음 왜냐면 작은 수를 곱한 후 더 큰게 나올 수 있음음