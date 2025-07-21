# 알고리즘 수업 - 선택 정렬 1
import sys
n, k = map(int, sys.stdin.readline().split())
lst = list(map(int, sys.stdin.readline().split()))

def selection(lst):
    cnt = 0
    result = -1

    for i in range(n-1, 0, -1):
        max_item, idx = lst[0], 0
        for j in range(1, i+1):
            if lst[j] > max_item:
                max_item, idx = lst[j], j

        if lst[i] != lst[idx]:
            lst[i], lst[idx] = lst[idx], lst[i]
            cnt += 1

        if cnt == k:
            result = f'{lst[idx]} {lst[i]}'
    
    return result

print(selection(lst))