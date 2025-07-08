N, K = map(int, (input().split()))
count = 0
while(True):
    if N == 1:
        break
    if N % K == 0:
        N = N//K
        count += 1
    else:
        N = N-1
        count += 1

print(count)


'''
주어진 N에 대해 최대한 많이 나누기를 수행해야한다.
- 항상 optimal solution을 보장할까?
N이 아무리 큰 수여도, K로 계속 나누면 기하급수적으로 빠르게 줄일 수 있다.
K가 2 이상이기만 하면, K로 나누는 것이 1을 빼는 것보다 항상 빠르게 N을 줄일 수 있다.
N은 항상 1에 도달하게 된다(최적의 해 성립)
'''