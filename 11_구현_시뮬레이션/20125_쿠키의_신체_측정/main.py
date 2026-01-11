#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 20125                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: jieunb_b <boj.kr/u/jieunb_b>                +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/20125                          #+#        #+#      #+#     #
#    Solved: 2025/03/18 18:00:26 by jieunb_b      ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
input = sys.stdin.readline

n = int(input())
board = [list(input().strip()) for _ in range(n)]
# 심장 위치 출력
# 왼쪽 팔, 오른쪽 팔, 허리, 왼쪽 다리, 오른쪽 다리 길이 출력

# 심장 찾고 위 아래로 가면서 계산하기
dx = [1,0,-1,0]
dy = [0,1,0,-1]

def heart_check(i,j):
    for k in range(4):
        if 0<=i+dy[k]<n and 0<=j+dx[k]<n:
            if board[i+dy[k]][j+dx[k]] != '*':
                return False
    return True

def heart():
    for i in range(n):
        for j in range(n):
            if board[i][j] == '*':
                if heart_check(i,j):
                    return i,j

def left_arm(y, x):
    cnt = 0
    for i in range(1, x+1):
        if board[y][x-i] == '*':
            cnt+=1
        else:
            break
    return cnt

def right_arm(y, x):
    cnt = 0
    for i in range(1, abs(n-x)):
        if board[y][x+i] == '*':
            cnt+=1
        else:
            break
    return cnt

def body(y, x):
    cnt = 0
    for i in range(1, abs(n-y)):
        if board[y+i][x] == '*':
            cnt+=1
            body_y, body_x = y+i, x
        else:
            break
    return cnt, body_y, body_x

def left_leg(y, x):
    cnt = 0
    for i in range(1, abs(n-y)):
        if board[y+i][x] == '*':
            cnt+=1
        else:
            break
    return cnt

def right_leg(y, x):
    cnt = 0
    for i in range(1, abs(n-y)):
        if board[y+i][x] == '*':
            cnt+=1
        else:
            break
    return cnt

y, x = heart() # [0]는 y, [1]는 x
print(y+1, x+1)

whole_body = []
# left_arm, x = x-1
whole_body.append(left_arm(y, x))
# right_arm, x = x+1   
whole_body.append(right_arm(y, x))
# body, y = y+1
cnt, body_y, body_x = body(y, x)
whole_body.append(cnt)
# left_leg
whole_body.append(left_leg(body_y, body_x-1))
# right_leg
whole_body.append(right_leg(body_y, body_x+1))

print(*whole_body)