#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 1283                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: jieunb_b <boj.kr/u/jieunb_b>                +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/1283                           #+#        #+#      #+#     #
#    Solved: 2025/05/23 11:12:27 by jieunb_b      ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
input = sys.stdin.readline

n = int(input())

def find(option, shortcut):
    for j, word in enumerate(option):
        for k in range(len(word)):
            if word[k].lower() not in shortcut:
                shortcut.add(word[k].lower())
                option[j] = (f'{word[:k]}[{word[k]}]{word[k+1:]}')
                return option
    return option

shortcut = set()
for i in range(n):
    option = list(input().split())
    check = False
    for j, word in enumerate(option):
        # 단어 첫 글자 확인
        if word[0].lower() not in shortcut:
            shortcut.add(word[0].lower())
            option[j] = (f'[{word[0]}]{word[1:]}')
            check = True
            break
    # 다 돌았는데도 없으면
    if not check:
        option = find(option, shortcut)
    print(' '.join(option))

