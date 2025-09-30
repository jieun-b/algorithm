#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 9017                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: jieunb_b <boj.kr/u/jieunb_b>                +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/9017                           #+#        #+#      #+#     #
#    Solved: 2025/03/22 01:05:46 by jieunb_b      ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
from collections import Counter
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    number = list(input().split())

    # 각 번호마다 개수 세기 -> 6이 아니면 점수 받을 수 없음
    # 순차적으로 점수 부여 후 각 팀의 점수 합이 가장 작은 팀 출력

    counter = Counter(number)
    score_dict = dict()
    
    count = 1
    for n in number: # 최대 1000번
        if counter[n] == 6:
            if n not in score_dict:
                score_dict[n] = [[count], count]
            else:
                if len(score_dict[n][0]) < 4:
                    score_dict[n][1] += count
                else: 
                    score_dict[n].append(count)
                score_dict[n][0].append(count)
            count += 1
    
    score_list = sorted(score_dict.items(), key= lambda x: (x[1][1], x[1][2]))
    print(score_list[0][0])   