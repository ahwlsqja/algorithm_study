# 로프
n = int(input())
lengths = [int(input()) for _ in range(n)]
lengths.sort()

result = 0
for i in range(n):
    val = lengths[i] * (n - i)
    result = max(result, val)

print(result)