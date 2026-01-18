import heapq

def solution(operations):
    max_heap = []
    min_heap = []
    for operation in operations:
        cmd, num = operation.split()
        if cmd == 'I':
            heapq.heappush(max_heap, -int(num))
            heapq.heappush(min_heap, int(num))
        elif max_heap != [] and min_heap != []:
            if num == '1':
                # 최댓값 삭제
                max_value = heapq.heappop(max_heap)
                min_heap.remove(-max_value)
            else:
                # 최솟값 삭제
                min_value = heapq.heappop(min_heap)
                max_heap.remove(-min_value)
    if max_heap and min_heap:
        return [-heapq.heappop(max_heap), heapq.heappop(min_heap)]
    else:
        return [0, 0]