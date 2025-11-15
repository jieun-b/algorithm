def solution(citations):
    answer = 0
    citations.sort(reverse=True)
    for i in range(len(citations)):
        if citations[i]-1 <= i:
            return max(citations[i], i)
    return len(citations)