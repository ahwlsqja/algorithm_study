K, N = map(int, input().split())

cables = []

for _ in range(K):
    cables.append(int(input()))

left = 1
right = max(cables)
answer = 0

while left <= right:
    mid = (left + right) // 2

    count = 0

    for cable in cables:
        count += cable // mid

    if count >= N:
        answer = mid
        left = mid + 1
    
    else:
        right = mid - 1

print(answer)