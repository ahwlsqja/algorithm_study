# 기타 레슨
import sys

N, M = map(int, sys.stdin.readline().split())
lessons = list(map(int, sys.stdin.readline().split()))

start, end = max(lessons), sum(lessons)
result = end
while start <= end:
    mid = (start + end) // 2
    cnt = 1
    total = 0

    for lesson in lessons:
        if total + lesson > mid:
            cnt += 1
            total = 0
        total += lesson

    if cnt <= M:
        result = mid
        end = mid - 1
    else: start = mid + 1

print(result)