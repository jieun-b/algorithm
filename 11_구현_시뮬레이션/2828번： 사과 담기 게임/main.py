#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 2828                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: jieunb_b <boj.kr/u/jieunb_b>                +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/2828                           #+#        #+#      #+#     #
#    Solved: 2024/05/27 01:40:39 by jieunb_b      ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

N, M = list(map(int, input().split()))
J = int(input())
order = []
for _ in range(J):
    order.append(int(input()))

basket = [0] * N
for i in range(M):
    basket[i] = 1

start = 0 # 현재 바구니 시작점
end = M-1 # 바구니 끝점
distance = 0
for i in range(J):
    apple = order[i]-1 # 사과 위치
    if start<=apple<=end:
        continue
    elif start > apple: 
        tmp = start-apple
        distance += tmp
        start = start-tmp
        end = end-tmp
    elif end < apple:
        tmp = apple-end
        distance += tmp
        start = start+tmp
        end = end+tmp
    
print(distance)