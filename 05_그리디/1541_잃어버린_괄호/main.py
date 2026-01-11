#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 1541                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: jieunb_b <boj.kr/u/jieunb_b>                +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/1541                           #+#        #+#      #+#     #
#    Solved: 2024/08/27 23:04:12 by jieunb_b      ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
input = sys.stdin.readline().rstrip()

result = ''
expression = input.split('-') # - 기준으로 자르기
for i, e in enumerate(expression):
    # e는 수 or 식 -> 모든 값 더함
    num = e.split('+')
    tmp = 0
    for n in num:
        tmp += int(n)
    
    if i == 0:
        result = result + str(tmp)
    else:
        result = result + '-(' + str(tmp) + ')'
print(eval(result))