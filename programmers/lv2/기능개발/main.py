def solution(arr):
    answer = []
    prev = -1
    for num in arr:
        if num != prev:
            prev = num
            answer.append(num)
    return answer