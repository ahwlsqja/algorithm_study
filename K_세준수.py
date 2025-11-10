# 입력
N = int(input())
K = int(input())

# 에라토스 테네스의 체
primeList = [True] * (N+1)  # 최대 1부터 N까지 소수 판별
for i in range(2, int(N**0.5)+1):
    if primeList[i]:  # i가 소수라면
        for j in range(2 * i, N+1, i):  # 2i부터 100까지 i의 배수들은 False
            primeList[j] = False

# N보다 작으면서 K이상인 소수의 배수들은 K-세준수가 아님
k_number = [1]*(N+1)
for i in range(2, N+1):
    if primeList[i] and i > K:
        for j in range(i, N+1, i):
            k_number[j] = 0
print(sum(k_number)-1)