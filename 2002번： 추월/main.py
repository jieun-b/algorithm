#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 2002                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: jieunb_b <boj.kr/u/jieunb_b>                +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/2002                           #+#        #+#      #+#     #
#    Solved: 2024/11/13 16:14:35 by jieunb_b      ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
# 추월한건지 밀린건지 어케 앎?
# 특정 번호가 원래 목록에서 다른 위치로 간 경우

# 맨 위부터 out 리스트에서 찾고 in 리스트에서 지우기
# 새로운 리스트 만들기

import sys
input = sys.stdin.readline

N = int(input())
t_in = []
t_out = []

for i in range(2*N):
    tmp = str(input().strip())
    if i >= N:
        t_out.append(tmp)
    else:
        t_in.append(tmp)

car = 0
while(t_in):
    if t_in == t_out:
        break
    for i in range(len(t_in)): 
        current = t_out[i]
        idx = t_in.index(current)
        if idx != i:
            t_out = t_out[i+1:]
            t_tmp = t_in[i:idx]
            if idx+1 != len(t_in):
                t_tmp.extend(t_in[idx+1:])
            t_in = t_tmp
            car += 1
            break
print(car)