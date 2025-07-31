# 숫자 카드
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

print(' '.join('1' if count_by_range(array, v, v) else '0' for v in res))