from collections import deque

def solution(bridge_length, weight, truck_weights):
    waiting_queue = deque(truck_weights)
    passing_queue = deque()
    time = 0
    
    while waiting_queue or passing_queue:
        time += 1
        if passing_queue and time - passing_queue[0][1] >= bridge_length:
            passing_queue.popleft()
        if waiting_queue:
            current_weight = sum(truck[0] for truck in passing_queue)
            if (current_weight + waiting_queue[0] <= weight and len(passing_queue) < bridge_length):
                truck_weight = waiting_queue.popleft()
                passing_queue.append((truck_weight, time))
                
    return time
