from collections import defaultdict
 
def solution(clothes):
    answer = 1
    info = defaultdict(int)
    for cloth in clothes:
        info[cloth[1]]+=1
    for cnt in info.values():
        answer *= (cnt+1)
    return answer - 1