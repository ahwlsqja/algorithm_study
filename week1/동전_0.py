
n, k = map(int, input().split())

# 동전의 가치들을 입력받아 리스트에 저장
coins = []
for _ in range(n):
    coins.append(int(input()))

# 가장 큰 동전부터 사용하기 위해 역순으로 정렬
coins.reverse()

count = 0
for coin in coins:
    if k >= coin:
        count += k // coin  # 해당 동전을 최대한 많이 사용
        k %= coin           # 남은 금액 계산
    
    if k == 0:  # 목표 금액을 만들었으면 종료
        break

print(count)