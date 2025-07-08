def solve_camping(L, P, V):
    # 완전한 사이클 수
    complete_cycles = V // P
    
    # 나머지 날짜
    remaining_days = V % P
    
    # 완전한 사이클에서 사용 가능한 날짜
    days_from_complete_cycles = complete_cycles * L
    
    # 나머지 날짜에서 사용 가능한 날짜 (최대 L일)
    days_from_remaining = min(remaining_days, L)
    
    return days_from_complete_cycles + days_from_remaining

case_num = 1
while True:
    line = input().strip()
    if line == "0 0 0":
        break
    
    L, P, V = map(int, line.split())
    result = solve_camping(L, P, V)
    print(f"Case {case_num}: {result}")
    case_num += 1