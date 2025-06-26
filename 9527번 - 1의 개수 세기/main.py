#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 9527                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: jieunb_b <boj.kr/u/jieunb_b>                +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/9527                           #+#        #+#      #+#     #
#    Solved: 2025/06/20 22:44:05 by jieunb_b      ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
input = sys.stdin.readline

a, b = map(int, input().split())
binary_one = [0 for _ in range(60)]

for i in range(1, 60):
    binary_one[i] = (1<<(i-1)) + (2*binary_one[i-1])

def count_one(n):
    count = 0
    while(0 < n):
        bin_n = bin(n)[2:]
        cur = len(bin_n) 
        prev = cur - 1 
        count += binary_one[prev]
        count += n-(1<<prev)+1
        n = n-(1<<prev)
    return count

print(count_one(b) - count_one(a-1))