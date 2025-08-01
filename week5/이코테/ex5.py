N = int(input())
array = list(map(int, input().split()))
dp = [0] * N
dp[0] = array[0]
for i in range(1, N):
    if array[i] >= array[i-1]:
        dp[i] = 0
    else:
        dp[i] = array[i]
count = 0
for i in dp:
    if i == 0:
        count += 1

print(count)