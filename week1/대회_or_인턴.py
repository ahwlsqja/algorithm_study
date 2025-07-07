N, M, K = map(int, input().split())

max_teams = 0
for i in range(K + 1):
    girls_to_intern = i
    boys_to_intern = K - i
    
    if girls_to_intern <= N and boys_to_intern <= M:
        remaining_girls = N - girls_to_intern
        remaining_boys = M - boys_to_intern
        teams = min(remaining_girls // 2, remaining_boys)
        max_teams = max(max_teams, teams)

print(max_teams)