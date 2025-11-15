def solution(n, m, x, y, r, c, k):
    answer = ''
    
    direction = [(1,0), (0,-1), (0,1), (-1,0)]
    alphabet = ['d', 'l', 'r', 'u']
    
    # x,y와 r,c의 직선 거리를 구해서 k 이상인 경우 무조건 불가능
    # 이동해야 하는 거리에서 직선 거리를 뺐을 때 남은 거리가 홀수인 경우 불가능
    distance = abs(x-r)+abs(y-c)
    if distance > k or (k-distance)%2==1:
        return "impossible"
    
    # k만큼 실행
        # 무조건 d 방향으로 가보기 -> 안되면 l로 
        # 안되는 경우는 범위에 벗어나거나 / 이동할 거리가 남은 이동할 거리보다 커지는 경우 / 남은 거리가 홀수인 경우
        # for 모든 방향
            # 되는 경우 break
    n_k = k        
    for _ in range(k):
        n_k -= 1
        for i in range(4):
            nx, ny = x+direction[i][0], y+direction[i][1]
            if 0<nx<=n and 0<ny<=m:
                distance = abs(nx-r)+abs(ny-c)
                if distance <= n_k and (n_k-distance)%2==0:
                    print(alphabet[i])
                    answer = answer+alphabet[i]
                    x, y = nx, ny
                    break

    return answer


# def solution(n, m, x, y, r, c, k):
#     answer = ''
    
#     direction = [(1,0), (0,-1), (0,1), (-1,0)]
#     alphabet = ['d', 'l', 'r', 'u']
    
#     def search(c_r, c_c, c_k, path):
#         nonlocal answer
#         if c_k > k:
#             return
#         if c_k == k:
#             if (c_r, c_c) == (r-1, c-1):
#                 if answer != "":
#                     answer = min(answer, path)
#                 else:
#                     answer = path
#             return
#         if answer != "" and answer[:c_k+1] < path[:c_k+1]:
#             return

#         # 문자열을 배열에 저장
#         for idx in range(4):
#             n_r, n_c = c_r + direction[idx][0], c_c + direction[idx][1]
#             if 0<=n_r<n and 0<=n_c<m:
#                 search(n_r, n_c, c_k+1, path+alphabet[idx])
    
#     search(x-1, y-1, 0, '')
#     if answer == "":
#         answer = "impossible"
#     return answer