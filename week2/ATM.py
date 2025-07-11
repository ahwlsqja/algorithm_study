n = int(input())
schedule_list = list(map(int, input().split()))
schedule_list.sort()

total_time = 0
cumulative_time = 0

for time in schedule_list:
    cumulative_time += time  # 현재까지 누적 시간
    total_time += cumulative_time  # 각 사람의 총 대기시간을 합산

print(total_time)