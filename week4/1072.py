# 게임
import sys

X, Y = map(int, sys.stdin.readline().split())
Z = (Y * 100) // X

if Z >= 99:
    print(-1)
else:
    start = 1
    end = 10**9
    answer = -1

    while start <= end:
        mid = (start + end) // 2
        new_z = ((Y + mid) * 100) // (X + mid)

        if new_z > Z:
            answer = mid
            end = mid - 1
        else:
            start = mid + 1

    print(answer)