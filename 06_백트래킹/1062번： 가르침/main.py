#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 1062                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: jieunb_b <boj.kr/u/jieunb_b>                +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/1062                           #+#        #+#      #+#     #
#    Solved: 2025/03/04 19:29:28 by jieunb_b      ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
input = sys.stdin.readline

n, k = list(map(int, input().split()))
words = [input().strip() for _ in range(n)]

# anta tica 를 포함하기 때문에 k는 최소 5가 되어야 함
if k < 5:
    print(0)
    exit()

# 비트마스크를 활용해 사용된 알파벳 저장
# 0~25의 비트가 각 알파벳을 나타냄
essential = {'a', 'c', 'n', 't', 'i'}

words_bitmask = [] # 특정 단어에서 사용된 알파벳
unique = set() # 전체 입력에서 등장한 알파벳
for word in words:
    word_bitmask = 0
    # 특정 단어에서 사용된 알파벳을 or 연산으로 누적해서 저장
    for char in set(word) - essential:
        word_bitmask |= (1 << (ord(char) - ord('a')))
        unique.add(char)
    words_bitmask.append(word_bitmask)
unique = list(unique)

if len(unique) < k-5:
    print(len(words))
    exit()

def search(idx, chosen, bitmask): # 현재 인덱스, 선택한 알파벳 개수, 현재 비트마스크
    global max_count
    if chosen == k-5:
        # 선택한 알파벳 조합으로 만들 수 있는 단어 확인
        count = 0
        for word_bitmask in words_bitmask:
            # 특정 단어에 대한 비트마스크와 현재 비트마스크의 연산 후 현재 비트마스크와 비교
            if (word_bitmask & bitmask) == word_bitmask:
                count += 1
        max_count = max(max_count, count)
        return
    for i in range(idx, len(unique)): # 특정 인덱스의 알파벳 하나 뽑기
        new_bitmask = bitmask | (1 << (ord(unique[i]) - ord('a')))
        search(i+1, chosen+1, new_bitmask)

# k개의 글자 중 필수 알파벳을 제외하면 k-5개 배울 수 있음
# 전체 입력에서 등장한 알파벳 중에 k-5개 알파벳 선택
# 선택된 개수가 k-5개 될 때까지 탐색
max_count = 0
search(0, 0, 0)
print(max_count)