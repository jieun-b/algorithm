def solution(brown, yellow):
    if yellow < 4:
        answer = [yellow+2, 3]
    else:
        for h in range(1, yellow):
            if yellow % h == 0:
                w = yellow//h
                if h > w:
                    break
                if (w*2 + h*2 + 4) == brown:
                    answer = [w+2, h+2]
    return answer