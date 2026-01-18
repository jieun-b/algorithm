def solution(n, lost, reserve):
    answer = n - len(lost)

    l = [False] * (n+1)
    r = [False] * (n+1)

    for num in lost:
        l[num] = True

    for num in reserve:
        if l[num]:
            l[num] = False
            answer += 1
        else:
            r[num] = True

    for i in range(1, n+1):
        if l[i]:
            if i > 1 and r[i-1]:
                r[i-1] = False
                answer += 1
            elif i < n and r[i+1]:
                r[i+1] = False
                answer += 1

    return answer
