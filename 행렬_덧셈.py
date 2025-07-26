N, M = map(int, input().split())

A = []
B = []
for i in range(N):
    A.append(list(map(int, input().split())))

for i in range(N):
    B.append(list(map(int, input().split())))


'''
sum_map = [[] for _ in range(N)]
for i in range(N):
    for j in range(M):
        sum_map[i].append(A[i][j] + B[i][j])
'''
for i in range(N):
    for j in range(M):
        print(A[i][j] + B[i][j], end=" ")
    print()