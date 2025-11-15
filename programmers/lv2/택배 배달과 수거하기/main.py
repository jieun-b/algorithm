def solution(cap, n, deliveries, pickups):
    answer = 0
    d_sum, p_sum = 0, 0
    
    # 뒤에서부터 돌면서 배달, 수거할 박스 개수 확인
    for i in range(n-1, -1, -1):
        d_sum += deliveries[i]
        p_sum += pickups[i]
        print(i, d_sum, p_sum)
        # 트럭에 넣을 수 있는 개수보다 많을 경우
        while d_sum > 0 or p_sum > 0:
            d_sum -= cap
            p_sum -= cap
            answer += (i + 1) * 2
            print(i, d_sum, p_sum, answer)
    return answer