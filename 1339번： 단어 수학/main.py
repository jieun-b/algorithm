#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 1339                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: jieunb_b <boj.kr/u/jieunb_b>                +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/1339                           #+#        #+#      #+#     #
#    Solved: 2025/02/20 21:45:23 by jieunb_b      ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
input = sys.stdin.readline

n = int(input())
words = [(input().strip()) for _ in range(n)]

alpha_weight = {}

# 모든 단어마다
for word in words:
    for i, char in enumerate(word):
        # 딕셔너리에 알파벳의 가중치 저장
        # 전체 합에 크게 관여할 수록 큰 값을 부여하는 것이 좋음
        if char in alpha_weight:
            alpha_weight[char] += 10**(len(word)-i-1)
        else:
            alpha_weight[char] = 10**(len(word)-i-1)

# 가중치가 높은 순서대로 9~0 할당
sorted_alpha = sorted(alpha_weight.items(), key=lambda x: x[1], reverse=True)
num_mapping = {char: 9 - i for i, (char, _) in enumerate(sorted_alpha)}

total_sum = 0
for word in words:
    tmp = ""
    for i, char in enumerate(word):
        tmp = tmp + str(num_mapping[char]) 
    total_sum += int(tmp)

print(total_sum)

# alphabets = list({words[i][j] for i in range(n) for j in range(len(words[i]))})
# visited = [False] * 10

# def operate():
#     result = 0
#     for i in range(n):
#         tmp = 0
#         for j in range(len(words[i])): # words[i][j]를 딕셔너리에서 찾아 값 입력
#             for k in range(len(alphabets)):
#                 if alphabets[k] == words[i][j]:
#                     tmp += dictionary[k] * (10**(len(words[i])-j-1))
#         result += tmp
#     return result

# def search(idx):
#     # 종료 조건
#     if idx == len(alphabets):
#         ans.append(operate())
#         return
#     for i in range(10):
#         if not visited[i]:
#             dictionary[idx] = i
#             visited[i] = True
#             search(idx+1)
#             visited[i] = False
#             dictionary[idx] = -1

# dictionary = [-1] * 10
# ans = [] # 모든 단어의 합 저장
# search(0) # 현재 알파벳 인덱스
# ans.sort()
# print(ans[-1])