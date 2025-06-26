#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 3687                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: jieunb_b <boj.kr/u/jieunb_b>                +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/3687                           #+#        #+#      #+#     #
#    Solved: 2025/06/23 17:54:41 by jieunb_b      ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
input = sys.stdin.readline

dp = [float('inf')]*101
number = [1, 7, 4, 2, 6, 8]
for i in range(6) :
  dp[i+2] = number[i]

for i in range(8, 101) :
  for j in range(2, i-1) :
    dp[i] = min(dp[i], int(str(dp[j]) + str(dp[i-j])))
    if j == 6 :
      dp[i] = min(dp[i], int(str(dp[i-j]) + '0'))

t = int(input())
for _ in range(t):
    n = int(input())
    # 가장 큰 수
    max_number = '1'*(n // 2)
    if n % 2 == 1:
        max_number = '7' + max_number[1:]
    # 가장 작은 수
    print(dp[n], max_number)

# ascend_number = sorted(number, key=lambda x: (x[1], -x[0]))
# discend_number = sorted(number, key=lambda x: (-x[1], x[0]))

# def find_min(tmp):
#     for i in range(10):
#         if discend_number[i][1] == tmp and discend_number[i][0] != 0:
#             return discend_number[i][0]

# def find_max(tmp):
#     for i in range(10): # 리스트 순회
#         if tmp - ascend_number[i][1] >= ascend_number[0][1]: 
#             tmp -= ascend_number[i][1]
#             return tmp, ascend_number[i][0]
#     for i in range(10):
#         if ascend_number[i][1] == tmp and ascend_number[i][0] != 0:
#             return -1, ascend_number[i][0]
    
# t = int(input())
# for _ in range(t):
#     n = int(input())
#     # 가장 큰 수 ascend_number
#         # 가장 개수가 적게 필요한 수 정렬
#         # 사용 후 남은 수가 가장 적은 개수보다 작으면 안됨, 다른 수로 넘어가
#         # 개수가 같을 경우 큰 수가 우선
#     tmp = n
#     max_number = []
#     while(True):
#         # 남은 수가 2보다 아래이면 종료
#         if tmp < ascend_number[0][1]:
#             break
#         # 남은 수가 2보다 크면
#         tmp, num = find_max(tmp)
#         max_number.append(str(num))
#     # 가장 작은 수 discend_number
#         # 최대한 개수가 많이 드는거 우선 7+8
#         # 사용 후 남은 수가 가장 적은 개수보다 작으면 안됨, 다른 수로 넘어가기
#         # 같을 때 작은 수가 우선, 대신 0은 안됨       
#     tmp = n
#     min_number = []
#     while(True):
#         # 남은 수가 7보다 아래이면 종료
#         if tmp <= discend_number[0][1]:
#             min_number.append(str(find_min(tmp)))
#             break
#         # 남은 수가 7보다 크면
#         for i in range(10): # 리스트 순회
#             if tmp - discend_number[i][1] >= discend_number[-1][1]: 
#                 min_number.append(str(discend_number[i][0]))
#                 tmp -= discend_number[i][1]
#                 break
#     print(''.join(reversed(min_number)), ''.join(reversed(max_number)))   