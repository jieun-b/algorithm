def solution(numbers):
    answer = 0
    visited = [False] * len(numbers)
    candidates = set()
    
    def search(cur):
        if cur:
            n = int(cur)
            if n > 1:
                candidates.add(n)

        for i in range(len(numbers)):
            if not visited[i]:
                visited[i] = True
                search(cur + numbers[i])
                visited[i] = False
                
    def find(num):
        for i in range(2, num):
            if num % i == 0:
                return False
        return True
        
    search('')    
    for num in list(candidates):
        if find(num):
            answer += 1
    return answer
