#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 2529                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: jieunb_b <boj.kr/u/jieunb_b>                +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/2529                           #+#        #+#      #+#     #
#    Solved: 2025/02/18 01:46:21 by jieunb_b      ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
input = sys.stdin.readline

k = int(input())
symbol = list(input().split())

# dfs로 풀 수 있음

# 조건 체크크
def check(a, b, symbol):
    if symbol == '<':
        if a < b:
            return True
    else:
        if a > b:
            return True
    return False

def search(current, equation):
    # 종료 조건
    if current == k+1:
        equations.append(equation)
        return
    
    # 현재 자리에 0~9중에 뭘 넣을지 선택
    for i in range(10):
        # 앞에서 사용한 숫자인지 확인
        if not visited[i]:
            # 현재 자리와 이전 자리 부등호 비교
            if current == 0 or check(equation[current-1], str(i), symbol[current-1]):
                visited[i] = True
                search(current+1, equation+str(i))
                visited[i] = False

visited = [False]*10
equations = []
search(0, '')
equations.sort()

print(equations[-1])
print(equations[0])
