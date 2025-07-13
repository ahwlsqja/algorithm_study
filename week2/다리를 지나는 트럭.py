# 다리를 지나는 트럭
from collections import deque

def solution(bridge_length, weight, truck_weights):
    time = 0
    bridge = deque([0] * bridge_length)
    truck_weights = deque(truck_weights)
    total_weight = 0

    while bridge:
        time += 1
        # 맨 앞 트럭 이동
        out = bridge.popleft()
        total_weight -= out

        # 다음 트럭 올릴 수 있는지 확인
        if truck_weights:
            if total_weight + truck_weights[0] <= weight:
                truck = truck_weights.popleft()
                bridge.append(truck)
                total_weight += truck
            else:
                bridge.append(0)  # 빈 자리 유지

    return time