#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 5568                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: jieunb_b <boj.kr/u/jieunb_b>                +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/5568                           #+#        #+#      #+#     #
#    Solved: 2025/09/18 16:50:52 by jieunb_b      ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
input = sys.stdin.readline

# 조합 만들기 -> 브루트포스
# k번 카드 선택 -> 이 때 카드 전체를 탐색하되 이미 사용한 카드인 경우 건너뛰기
n = int(input())
k = int(input())
cards = [input().strip() for _ in range(n)]
visited = [False]*n
all_set = set()

def search(current, made):
    if current == k:
        all_set.add(made)
        return
    for i in range(n):
        if not visited[i]:
            visited[i] = True
            search(current+1, made+cards[i])
            visited[i] = False

search(0, '')
print(len(all_set))

# import sys
# from itertools import permutations
# input = sys.stdin.readline

# n = int(input())
# k = int(input())
# cards = [input().strip() for _ in range(n)]

# # k개를 뽑는 순열 생성
# all_case = set("".join(p) for p in permutations(cards, k))

# print(len(all_case))