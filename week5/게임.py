def solve_game_winrate(X, Y):
    win_rate = (Y * 100) // X

    if win_rate >= 99:
        return -1
    
    left, right = 1, X
    answer = -1

    while left <= right:
        mid = (left + right) // 2

        new_rate = ((Y + mid) * 100) // (X + mid)

        if new_rate > win_rate:
            answer = mid
            right = mid - 1

        else:
            left = mid + 1

    return answer
X, Y = map(int, input().split())
result = solve_game_winrate(X, Y)
print(result)
