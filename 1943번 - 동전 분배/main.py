#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 1943                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: jieunb_b <boj.kr/u/jieunb_b>                +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/1943                           #+#        #+#      #+#     #
#    Solved: 2025/06/19 16:32:43 by jieunb_b      ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
from collections import defaultdict
input = sys.stdin.readline

for _ in range(3):
    n = int(input())
    total_coin = defaultdict(int)
    money = 0
    for i in range(1, n+1): 
        coin, num = map(int, input().split())
        money += coin * num
        total_coin[coin] = num
    if money % 2 == 1:
        print(0)
        continue
    
    half = money//2
    dp = [False] * (half+1)
    dp[0] = True

    for coin, num in total_coin.items(): # 특정 동전으로 만들 수 있는 경우 체크
        for find in range(half, coin - 1, -1):
            if dp[find - coin]: # 처음에 작은 수에 걸림 -> 100원
                for i in range(num):
                    if find + coin*i <= half:
                        dp[find + coin*i] = True
    if dp[half]:
        print(1)
    else:
        print(0)
        

# import sys
# from collections import defaultdict
# input = sys.stdin.read

# data = list(map(int, input().split()))
# idx = 0
# while(idx < len(data)):
#     n = data[idx]
#     total_coin = defaultdict(int)
#     money = 0
#     for i in range(1, n+1): 
#         coin, num = data[idx+(2*i-1)], data[idx+(2*i)] 
#         money += coin * num
#         total_coin[coin] = num
#     if money % 2 == 1:
#         print(0)
#         idx = idx + n*2 + 1
#         continue
#     half = money//2
#     dp = [False] * (half+1)
#     dp[0] = True

#     for coin, num in total_coin.items():
#         for _ in range(num):
#             for j in range(half, coin - 1, -1):
#                 if dp[j - coin]:
#                     dp[j] = True

#     if dp[half]:
#         print(1)
#     else:
#         print(0)
#     idx = idx + n*2 + 1
