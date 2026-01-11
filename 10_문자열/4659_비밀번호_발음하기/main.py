#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 4659                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: jieunb_b <boj.kr/u/jieunb_b>                +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/4659                           #+#        #+#      #+#     #
#    Solved: 2025/03/18 16:39:22 by jieunb_b      ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
input = sys.stdin.readline

vowel = ['a', 'e', 'i', 'o', 'u']
while True:
    check = False
    test_case = input().strip()
    # 종료
    if test_case == 'end':
        exit()
    # 다 모음이 아닌 경우
    if all(v not in test_case for v in vowel):
        check = True
    else:
        three, prev_char = 0, ''
        for char in list(test_case):
            if prev_char != '':
                # 같은 글자 연속인 경우
                if prev_char == char and not (char == 'e' or char == 'o'):
                    check = True
                    break
                if (prev_char in vowel) == (char in vowel): # 이전 글자랑 현재 글자가 자, 모 같을 때
                    three += 1
                else:
                    three = 1
                    prev_char = char
            else:
                three = 1
                prev_char = char
            if three == 3:
                check = True
                break
    if not check:
        print(f'<{test_case}> is acceptable.')
    else:
        print(f'<{test_case}> is not acceptable.')  