def solution(today, terms, privacies):
    answer = []
    t_y, t_m, t_d = map(int, today.split('.'))
    # 약관에 따른 유효기간 저장
    months = dict()
    for term in terms:
        alphabet, month = term.split()
        months[alphabet] = int(month)
    # 수집된 개인정보를 돌면서 파기해야 하는지 확인
    for i, privacy in enumerate(privacies):
        date, alphabet = privacy.split()
        y, m, d = map(int, date.split('.'))
        # 개인정보 수집 일자 + 약관 기간 -> months[alphabet]이 m에 더할 수
        # m이 12를 넘어가면 y를 +1, d에서 -1을 하는데 0인 경우 28이 되고 m을 +1
        d -= 1
        if d == 0:
            d = 28
            m -= 1
        m += months[alphabet]
        while m > 12:
            m -= 12
            y += 1
        # 현재 날짜와 비교 
        if t_y > y:
            answer.append(i+1)
        elif t_y == y:
            if t_m > m:
                answer.append(i+1)
            elif t_m == m:
                if t_d > d:
                    answer.append(i+1)
    return answer