# 나무 자르기
import sys

n, m = list(map(int, sys.stdin.readline().split(' ')))
array = list(map(int, sys.stdin.readline().split()))


start, end = 0, max(array)
result = 0
while start <= end:
    total = 0
    mid = (start + end) // 2

    for x in array:
        if x > mid:
            total += x - mid
    
    if total < m:
        end = mid - 1
    else:
        result = mid
        start = mid + 1

print(result)