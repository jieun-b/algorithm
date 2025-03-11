#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 8979                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: jieunb_b <boj.kr/u/jieunb_b>                +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/8979                           #+#        #+#      #+#     #
#    Solved: 2025/03/11 14:07:38 by jieunb_b      ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
input = sys.stdin.readline

n, k = map(int, input().split())

countries = []
for _ in range(n):
    info = list(map(int, input().split()))
    countries.append((info[0], info[1], info[2], info[3]))

countries.sort(key=lambda x: (-x[1], -x[2], -x[3]))

# K번 국가의 등수 찾기
rank = 1
for i in range(n):
    if countries[i][0] == k:
        target = countries[i]  # K번 국가의 메달 정보
        break

# 동일한 메달 개수를 가진 국가들의 등수 처리
for i in range(n):
    if countries[i][1:] == target[1:]:  # 메달 정보가 같으면 같은 등수
        print(i + 1)
        break


# nation = dict()
# for _ in range(n):
#     info = list(map(int, input().split()))
#     nation[info[0]] = info[1:]

# nation = sorted(nation.items(), key=lambda x:x[1][2], reverse=True)
# nation = sorted(nation, key=lambda x:x[1][1], reverse=True)
# nation = sorted(nation, key=lambda x:x[1][0], reverse=True)
# medal = dict(nation)[k]

# seen = []
# for i in range(n):
#     if nation[i][1] not in seen:
#         seen.append(nation[i][1])
#     if nation[i][1] == medal:
#         break
# print(len(seen))