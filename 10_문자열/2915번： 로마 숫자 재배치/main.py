#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 2915                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: jieunb_b <boj.kr/u/jieunb_b>                +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/2915                           #+#        #+#      #+#     #
#    Solved: 2024/09/04 23:03:05 by jieunb_b      ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
input = sys.stdin.readline().rstrip()

init = input
result = init

one = ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX']
ten = ['X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC']


if 'VI' in init and not 'VII' in init:
    result = init.replace('VI', 'IV')
if 'LX' in init and not 'LXX' in init:
    result = result.replace('LX', 'XL')
if 'XI' in init and not 'XII' in init and not 'XIV' in init and not 'XIX' in init:
    result = result.replace('XI', 'IX')
if 'LXXI' == init:
    result = 'XLIX'
print(result)
