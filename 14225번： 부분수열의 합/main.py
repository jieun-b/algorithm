#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 14225                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: jieunb_b <boj.kr/u/jieunb_b>                +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/14225                          #+#        #+#      #+#     #
#    Solved: 2025/02/25 16:43:21 by jieunb_b      ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
input = sys.stdin.readline

n = int(input())
s = list(map(int, input().split()))
s.sort()  # 작은 숫자부터 정렬

min_num = 1  # 만들 수 없는 최소 양의 정수 초기값

for num in s:
    print('원소',num)
    print('최소 합',min_num)
    if min_num < num:  # 현재 만들 수 있는 범위를 벗어나면 종료
        break
    min_num += num  # 현재 숫자를 추가하여 만들 수 있는 범위를 확장

print(min_num)

# min_num = 0
    
# def sub_sum(idx): 
#     for i in range(idx, n):
#         sub_list.append(s[i])
#         if not sum(sub_list) in all_sub_list:
#             all_sub_list.append(sum(sub_list))
#         sub_sum(i+1)
#         sub_list.pop()

# sub_list = [] # 특정 부분 집합
# all_sub_list = [] # 부분 집합의 합에 대한 전체 리스트
# sub_sum(0) 

# all_sub_list.sort()

# min_num = 1
# for num in all_sub_list:
#     if min_num != num:
#         break
#     min_num += 1
# print(min_num)