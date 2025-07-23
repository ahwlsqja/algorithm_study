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
        A[last], A[max_idx] = A[max_idx], A[last]
        if cnt == k:
            print(*A)
            exit()


print(-1)