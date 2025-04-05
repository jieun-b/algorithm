#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 1244                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: jieunb_b <boj.kr/u/jieunb_b>                +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/1244                           #+#        #+#      #+#     #
#    Solved: 2025/03/21 23:54:21 by jieunb_b      ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
input = sys.stdin.readline

# 남이면 입력의 배수만 바꾸기기
# 여이면 양쪽이 같은지 확인하고 바꾸기 없으면 본인만

switch_num = int(input())
states = list(map(int, input().split()))

student_num = int(input())
students = [list(map(int, input().split())) for _ in range(student_num)]

for sex, num in students:
    if sex == 1: # 남
        for i in range(num - 1, switch_num, num):
            states[i] = 1 - states[i]
    else: # 여
        num -= 1
        states[num] = 1 - states[num]
        left, right = num - 1, num + 1
        while left >= 0 and right < switch_num and states[left] == states[right]:
            states[left] = 1 - states[left]
            states[right] = 1 - states[right]
            left -= 1
            right += 1
            
for i in range(0, switch_num, 20):
    print(*states[i:i+20])