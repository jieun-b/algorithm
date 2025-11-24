# from collections import deque

# def solution(n, wires):
#     answer = float('inf')
    
#     graph = [[] for _ in range(n+1)]
#     for a, b in wires:
#         graph[a].append(b)
#         graph[b].append(a)
    
#     def search(a, b):
#         queue = deque([a])
#         visited[a] = True
#         net = []
#         while queue:
#             cur = queue.popleft()
#             net.append(cur)
#             for i in range(len(graph[cur])):
#                 next = graph[cur][i]
#                 if next != b and not visited[next]:
#                     queue.append(next)
#                     visited[next] = True
#         return len(net)
    
#     for a, b in wires:
#         visited = [False]*(n+1)
#         cnt = search(a, b)
#         diff = abs(2*cnt-n)
#         answer = min(answer, diff)
        
#     return answer


def solution(n, wires):
    answer = float('inf')
    
    graph = [[] for _ in range(n+1)]
    for a, b in wires:
        graph[a].append(b)
        graph[b].append(a)
    
    visited = [False] * (n+1)
    sub = [0] * (n+1)
    
    def search(node):
        visited[node] = True
        size = 1
        for next in graph[node]:
            if not visited[next]:
                size += search(next)
        sub[node] = size
        return size
        
    search(1)
    
    for a, b in wires:
        child_sub = min(sub[a], sub[b])
        diff = abs(n - 2 * child_sub)
        answer = min(answer, diff)

    return answer