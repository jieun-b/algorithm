#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 2564                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: jieunb_b <boj.kr/u/jieunb_b>                +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/2564                           #+#        #+#      #+#     #
#    Solved: 2024/07/02 22:40:08 by jieunb_b      ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
input = sys.stdin.readline

w, h = map(int, input().split())
n = int(input())
store = [list(map(int, input().split())) for _ in range(n)]
dong = list(map(int, input().split()))

res = 0
if dong[0] == 1:
    for direction, distance in store: 
        if direction == 1:
            res += abs(distance - dong[1])
        elif direction == 2:
            right = (w-distance) + (w-dong[1])
            left = distance + dong[1]
            res += (h+min(right,left))
        elif direction == 3:
            res += dong[1]+distance
        else:
            res += (w-dong[1])+distance
elif dong[0] == 2:
    for direction, distance in store: 
        if direction == 1:
            right = distance + dong[1]
            left = (w-distance) + (w-dong[1])
            res += (h+min(right,left))
        elif direction == 2:
            res += abs(distance - dong[1])
        elif direction == 3:
            res += dong[1]+(h-distance)
        else:
            res += (w-dong[1])+(h-distance)
elif dong[0] == 3:
    for direction, distance in store: 
        if direction == 1:
            res += dong[1]+distance
        elif direction == 2:
            res += (h-dong[1])+distance
        elif direction == 3:
            res += abs(distance - dong[1])
        else:
            right = distance + dong[1]
            left = (h-distance) + (h-dong[1])
            res += (w+min(right,left))
else:
    for direction, distance in store: 
        if direction == 1:
            res += dong[1]+(w-distance)
        elif direction == 2:
            res += (h-dong[1])+(w-distance)
        elif direction == 3:
            right = (h-distance) + (h-dong[1])
            left = distance + dong[1]
            res += (w+min(right,left))
        else:
            res += abs(distance - dong[1])
print(res)