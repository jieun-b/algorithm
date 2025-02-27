#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 6603                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: jieunb_b <boj.kr/u/jieunb_b>                +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/6603                           #+#        #+#      #+#     #
#    Solved: 2025/02/21 18:45:10 by jieunb_b      ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
input = sys.stdin.readline

def check(string, num):
    if int(string[-1]) < int(num):
        return True
    else:
        return False

def search(k, s, idx, string): # 선택한 수의 개수, 집합에 포함되는 수, 선택한 수
    if idx == 6:
        print(*string)
        return
    for i in range(k):
        if not visited[i]:
            if idx == 0 or check(string, s[i]):
                visited[i] = True
                string.append(s[i])
                search(k, s, idx+1, string)
                string.pop()
                visited[i] = False

while True:
    testcase = input().strip()
    if testcase == "0":
        break
    testcase = testcase.split()
    k = int(testcase[0])
    s = list(testcase[1:k+1])
    visited = [False]*k
    string = []
    search(k, s, 0, string)
    print()