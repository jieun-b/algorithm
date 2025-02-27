# 음료수 얼려 먹기

n, m = map(int, input().split())

graph = []
for i in range(n):
    graph.append(list(map(int, input())))

def dfs(i, j):
    if graph[i][j] == 1:
        return False
    graph[i][j] = 1
    if i-1 >= 0: dfs(i-1, j)
    if i+1 < n: dfs(i+1, j)
    if j-1 >= 0: dfs(i, j-1)
    if j+1 < m: dfs(i, j+1)
    return True

count = 0
for i in range(n):
    for j in range(m):
        check = dfs(i, j)
        if check:
            count += 1

print(count)