# 알고리즘 수업 - 퀵 정렬 1
import sys
sys.setrecursionlimit(int(10**6))

def partition(lst, start, end):
    global cnt
    pivot = lst[end]
    i = start-1
    for j in range(start,end): 
        if lst[j] <= pivot: 
            i +=1
            lst[i], lst[j] = lst[j], lst[i]
            cnt += 1
            if cnt == k: print(lst[i],lst[j])

    if i+1 != end:
        lst[i+1], lst[end] = lst[end], lst[i+1]
        cnt += 1
        if cnt == k: print(lst[i+1],lst[end])
    return i+1

def quick_sort(lst, start, end):
    if start >= end: return
    q = partition(lst,start,end)
    quick_sort(lst,start,q-1)
    quick_sort(lst,q+1,end)

n,k = map(int,sys.stdin.readline().split())
lst = list(map(int,sys.stdin.readline().split()))
cnt = 0

quick_sort(lst, 0, n-1)

if cnt < k: print(-1)