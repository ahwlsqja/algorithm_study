# 알고리즘 수업 - 삽입 정렬 1
import sys

n, k = map(int, sys.stdin.readline().split())
lst = list(map(int, sys.stdin.readline().split()))

def insertion_sort(lst, K):
    cnt = 0

    for i in range(1, len(lst)):
        loc = i - 1
        newItem = lst[i]

        while loc >= 0 and newItem < lst[loc]:
            cnt += 1
            lst[loc + 1] = lst[loc]
            loc -= 1

            if cnt == K:
                print(lst[loc + 1])
                return

        if loc + 1 != i:
            cnt += 1
            lst[loc + 1] = newItem

            if cnt == K:
                print(lst[loc + 1])
                return

    print(-1)

insertion_sort(lst, k)