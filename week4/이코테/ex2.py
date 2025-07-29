N, x = map(int, input().split())

ls = list(map(int, input().split()))

from bisect import bisect_left, bisect_right

def count_by_range(ls, left_value, right_value):
    right_index = bisect_right(ls, right_value)
    left_index = bisect_left(ls, left_value)
    return right_index - left_index

if x in ls:
    print(count_by_range(ls, x, x))
else:
    print(-1)