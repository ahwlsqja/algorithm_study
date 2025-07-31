# 예산
import sys

N = int(sys.stdin.readline())
array = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())

start, end = 0, max(array)
answer = 0
while start <= end:
    mid = (start + end) // 2

    total = 0
    for x in array:
        if x > mid:
            total += mid
        else:
            total += x

    if total <= M:
        answer = mid
        start = mid + 1
    else:
        end = mid - 1

print(answer)
