def solution(numbers, target):
    answer = 0
    
    def search(idx, num):
        nonlocal answer
        if idx == len(numbers):
            if num == target:
                answer+=1
            return
        search(idx+1, num+int('+'+str(numbers[idx])))
        search(idx+1, num+int('-'+str(numbers[idx])))
        
    search(0, 0)
        
    return answer