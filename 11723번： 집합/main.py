#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 11723                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: jieunb_b <boj.kr/u/jieunb_b>                +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/11723                          #+#        #+#      #+#     #
#    Solved: 2025/03/09 14:21:51 by jieunb_b      ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
input = sys.stdin.readline

m = int(input())

result = set()
for _ in range(m):
    cmd = input().split()
    command = cmd[0]
    if len(cmd) != 1:
        num = int(cmd[1])
    if command == 'add':
        if num not in result:
            result.add(num)
    elif command == 'remove':
        if num in result:
            result.remove(num)
    elif command == 'check':
        if num in result:
            print(1)
        else:
            print(0)
    elif command == 'toggle':
        if num in result:
            result.remove(num)
        else:
            result.add(num)
    elif command == 'all':
        result = {1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20}
    elif command == 'empty':
        result = set()