n, k = map(int, input().split())
A = list(map(int, input().split()))

cnt = 0
for last in range(n-1, 0, -1):
    max_idx = 0
    for i in range(last + 1):
        if A[i] > A[max_idx]:
            max_idx = i
    
    if last != max_idx:
        cnt += 1
        if cnt == k:
            print(min(A[last], A[max_idx]), max(A[last], A[max_idx]))
            exit()
        A[last], A[max_idx] = A[max_idx], A[last]

print(-1)