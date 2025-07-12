from collections import deque

T = int(input())

for _ in range(T):
    N, M = map(int, input().split())
    prioritie = list(map(int, input().split()))

    queue = deque()
    for i in range(N):
        queue.append((prioritie[i], i))

    print_count = 0

    while queue:
        current = queue.popleft()
        current_priority, current_index = current
        has_higher_priority = False
        for priority, _ in queue:
            if priority > current_priority:
                has_higher_priority = True
                break

        if has_higher_priority:
            queue.append(current)

        else: 
            print_count += 1
        
            if current_index == M:
                print(print_count)
                break
