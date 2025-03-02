#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 14501                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: jieunb_b <boj.kr/u/jieunb_b>                +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/14501                          #+#        #+#      #+#     #
#    Solved: 2025/03/02 17:29:23 by jieunb_b      ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
input = sys.stdin.readline

n = int(input())
tp = [list(map(int, input().split())) for _ in range(n)]

# def search(idx, add, value): # 현재 날짜, 현재까지 금액 
#     global max_value
#     max_value = max(max_value, value)
#     for i in range(idx+add, n):
#         if i+tp[i][0] <= n:
#             search(i, tp[i][0], value+tp[i][1])

# max_value = 0
# for i in range(n):
#     search(i, tp[i][0], tp[i][1])
# print(max_value)


def search(idx, value):
    global max_value
    # 현재 날짜가 마지막 날짜를 넘지 않으면 최대 금액을 갱신
    if idx >= n:
        max_value = max(max_value, value)
        return
    # 현재 날짜에서 이 일을 했을 때
    if idx + tp[idx][0] <= n:  # 이 일을 끝낼 수 있는 경우
        search(idx + tp[idx][0], value + tp[idx][1])
    # 현재 날짜에서 이 일을 하지 않은 경우
    search(idx + 1, value)

max_value = 0
search(0, 0)
print(max_value)  