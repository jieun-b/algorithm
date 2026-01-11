#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 10431                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: jieunb_b <boj.kr/u/jieunb_b>                +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/10431                          #+#        #+#      #+#     #
#    Solved: 2025/03/10 11:53:14 by jieunb_b      ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
input = sys.stdin.readline

p = int(input())

def alignment(idx, count, height):
    while True:
        tmp = height[idx]
        height[idx], height[idx-1] = height[idx-1], tmp
        idx -= 1
        count += 1
        if idx == 0 or height[idx-1] < height[idx]:
            break
    return count, height

for _ in range(p):
    test_case = list(map(int, input().split()))
    num, height = test_case[0], test_case[1:]
    count = 0
    for i in range(1, 20): # 1에서 19번 인덱스까지
        if height[i] < height[i-1]: # 앞에 키 큰 학생이 있는 경우
  
            count, height = alignment(i, count, height)
    print(num, count)