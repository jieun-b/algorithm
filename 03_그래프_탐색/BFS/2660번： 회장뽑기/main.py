#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 2660                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: jieunb_b <boj.kr/u/jieunb_b>                +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/2660                           #+#        #+#      #+#     #
#    Solved: 2024/10/10 00:13:40 by jieunb_b      ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
input = sys.stdin.readline

member = int(input())
relations = [[] for _ in range(member+1)]
while(True):
    relation = list(map(int, input().split()))
    if relation == [-1, -1]:
        break
    else:
        relations[relation[0]].append(relation[1])
        relations[relation[1]].append(relation[0])

def check(i, friends, score): #3, [1, 3, 4]
    print(i, friends, score)
    # if score > member:
    #     return score
    if i in friends:
        return score
    else:
        for j in friends:
            if visited[j] == 0:
                visited[j] = 1
                score = check(i, relations[j], score+1)
        return score

res = [0 for _ in range(member+1)]
for i in range(1,member+1): # 회장 후보 1
    score = 1
    for j in range(1,member+1): # 친구 확인 3
        if i != j:
            print('i,j', i, j)
            visited = [0 for _ in range(member+1)]
            visited[0] = 1
            visited[i] = 1
            score = max(check(j, relations[i], 1), score)  # 3, [2], 1
    res[i-1] = score

print(res)