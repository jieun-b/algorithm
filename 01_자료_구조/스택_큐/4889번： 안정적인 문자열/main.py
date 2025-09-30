#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 4889                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: jieunb_b <boj.kr/u/jieunb_b>                +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/4889                           #+#        #+#      #+#     #
#    Solved: 2024/06/25 22:51:04 by jieunb_b      ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
input = sys.stdin.readline

num = 0 
while(True):
    sen = input()
    if '-' in sen:
        break

    num += 1
    store = []
    count = 0
    for s in sen:
        if s == '{':
            store.append(s)
        elif s == '}':
            if store:
                store.pop()
            else:
                count += 1
                store.append(s)
    count += len(store)//2
    
    print(str(num)+'.', count)
