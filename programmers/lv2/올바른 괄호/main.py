def solution(s):
    answer = True
    
    queue = []
    for c in s:
        if c == '(':
            queue.append('(')
        else:
            if queue == []:
                return False
            else:
                queue.pop()
    if queue == []:
        return True
    else:
        return False