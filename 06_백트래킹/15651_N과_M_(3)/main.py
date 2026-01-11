#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 15651                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: jieunb_b <boj.kr/u/jieunb_b>                +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/15651                          #+#        #+#      #+#     #
#    Solved: 2024/06/04 16:36:31 by jieunb_b      ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

def search(res):
    for i in range(1,N+1):
        res.append(i)
        if len(res) < M:
            search(res)
        else:
            print(*res)
            res.pop()
            continue
        res.pop()

N, M = list(map(int, input().split()))

for i in range(1, N+1):
    res = []
    res.append(i)
    if len(res) < M:
        search(res)
    else:
        print(*res)
        continue
    
