from collections import deque
def solution(bridge_length, weight, truck_weights):
    bridge = deque([0 for _ in range(bridge_length)])
    cur_weight = 0
    cnt = 0
    while(truck_weights):
        cnt += 1
        cur_weight -= bridge.popleft()
        if truck_weights[0] + cur_weight <= weight:
            bridge.append(truck_weights[0])
            cur_weight += truck_weights[0]
            truck_weights = truck_weights[1:]
        else:
            bridge.append(0)
    return cnt + bridge_length