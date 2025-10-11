#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 1920                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: jieunb_b <boj.kr/u/jieunb_b>                +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/1920                           #+#        #+#      #+#     #
#    Solved: 2025/10/11 23:18:10 by jieunb_b      ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
m = int(input())
check = list(map(int, input().split()))

a.sort()
for i in range(m):
    start, end = 0, n-1
    exist = 0
    while(start <= end):
        idx = (start+end) // 2 
        if check[i] == a[idx]:
            exist = 1
        if check[i] > a[idx]: 
            start = idx+1
        else:
            end = idx-1
    print(exist)