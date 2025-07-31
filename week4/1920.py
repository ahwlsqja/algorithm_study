# 수 찾기
import sys
from bisect import bisect_left, bisect_right

def count_by_range(array, left_value, right_value):
    right_index = bisect_right(array, right_value)
    left_index = bisect_left(array, left_value)
    return right_index - left_index

_ = sys.stdin.readline()
array = list(map(int, sys.stdin.readline().split()))
_ = sys.stdin.readline()
res = list(map(int, sys.stdin.readline().split()))
array.sort()

for v in res:
    cnt = count_by_range(array, v, v)
    if cnt == 0: print(0)
    else: print(1)