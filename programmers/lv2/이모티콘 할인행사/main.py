
def solution(users, emoticons):
    
    def search(users, emoticons, sales): # 사용자 조건, 이모티콘 가격, 이모티콘 할인
        nonlocal plus
        nonlocal cost
        if len(sales) == len(emoticons): # 이모티콘 할인 정보가 다 채워졌을 때
            new_plus, new_cost = 0, 0
            for i in range(len(users)): # 사용자의 플러스 가입 여부, 구매 비용 기록
                tmp = 0
                for j in range(len(emoticons)): # 이모티콘 가격
                    if sales[j] >= users[i][0]: # 이모티콘 할인율이 사용자의 비율보다 크거나 같을 때
                        tmp += emoticons[j]*((100-sales[j])/100)
                if tmp >= users[i][1]: # 플러스 구입이 나을 경우
                    new_plus += 1
                else:
                    new_cost += tmp
            if new_plus > plus:
                plus = new_plus
                cost = new_cost
            elif new_plus == plus:
                cost = max(cost, new_cost)
            return
        for sale in range(1, 5): # 할인율 선택
            sales.append(sale*10)
            search(users, emoticons, sales)
            sales.pop()
    
    plus, cost = 0, 0
    search(users, emoticons, []) 
    answer = [plus, cost]
    return answer