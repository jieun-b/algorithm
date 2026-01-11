#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 20437                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: jieunb_b <boj.kr/u/jieunb_b>                +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/20437                          #+#        #+#      #+#     #
#    Solved: 2025/05/25 15:52:21 by jieunb_b      ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
from collections import defaultdict
input = sys.stdin.readline

t = int(input())
for _ in range(t): # 테스트케이스
    w = input().strip()
    k = int(input())
   
    pos_dict = defaultdict(list)
    for idx in range(len(w)):
        pos_dict[w[idx]].append(idx)
   
    if all(len(pos_dict[alphabet]) < k for alphabet in pos_dict):
        print(-1)
        continue

    min_string = 10001
    max_string = 0
    for alphabet in pos_dict:
        pos_list = pos_dict[alphabet]
        if len(pos_list) >= k:
            for i in range(len(pos_list)-k+1):
                min_string = min(pos_list[i+k-1] - pos_list[i] + 1, min_string)
                max_string = max(pos_list[i+k-1] - pos_list[i] + 1, max_string)
    print(min_string, max_string)

# t = int(input())
# for _ in range(t): # 테스트케이스
#     w = input().strip()
#     k = int(input())
#     count = Counter(w)
#     if all(count[alphabet] < k for alphabet in count.keys()):
#         print(-1)
#         continue

#     min_string = 10001
#     max_string = 0
#     for i in range(len(w)): # 문자하나씩 -> 최대 10000번
#         if count[w[i]] < k :
#             continue
#         # print('w[i]', w[i])
#         condition = 1
#         for j in range(i+1, len(w)): # 범위확인 -> 최대 10000번
#             if w[i] == w[j]:
#                 condition += 1
#             if condition == k:
#                 min_string = min(j-i+1, min_string)
#                 max_string = max(j-i+1, max_string)
#                 break
#         # print('min_string', min_string)
#         # print('max_string', max_string)
#     print(min_string, max_string)