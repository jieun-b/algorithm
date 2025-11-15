def solution(numbers):
    answer = []
    # 주어진 십진수를 이진수로 변환한 뒤
    # 왼쪽부터 노드에 수를 넣는다고 했을 때
    # 만들어 질 수 있는 유형인지 확인
    def search(arr, zero):
        nonlocal ans
        root = len(arr)//2
        if arr[root] == '0': # 더미 노드일 때
            zero = True
        else: # 더미 노드가 아닐 때
            if zero:
                ans = 0
        if len(arr) == 1:
            return
        left = arr[:root]
        right = arr[root+1:]
        search(left, zero)
        search(right, zero)

    for number in numbers:
        bin_num = bin(number)[2:]
        n = 1
        while True:
            n *= 2
            if n-1 >= len(bin_num):
                break
        bin_num = '0'*(n-1-len(bin_num))+bin_num
        ans = 1
        search(bin_num, False)
        answer.append(ans)
        
    return answer