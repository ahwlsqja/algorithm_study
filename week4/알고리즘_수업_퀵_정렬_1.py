import sys
input = lambda: sys.stdin.readline().rstrip()
sys.setrecursionlimit(10**4) #RecursionError 방지
N, K = map(int, (input().split()))
ls = list(map(int, input().split()))
count = 0
found = False

def quick_sort(A, p, r):
    if found or p>=r: #원소가 1개인 경우 종료
        return
    if(p<r):
        q = partition(A, p, r)
        quick_sort(A, p, q-1)
        quick_sort(A, q+1, r)

def partition(A, p, r):
    global count
    if found:
        return r
    
    x = A[r] #pivot
    i = p-1
    for j in range(p, r):
        if A[j] <= x:
            i += 1
            A[i], A[j] = A[j], A[i]
            count += 1
            if count == K:
                print(A[i], A[j])
    
    if i+1 != r:
        A[i+1], A[r] = A[r], A[i+1]
        count +=1 
        if count == K:
            print(A[i+1], A[r])
    return i+1

quick_sort(ls, 0, N-1)
if count < K:
    print(-1)
