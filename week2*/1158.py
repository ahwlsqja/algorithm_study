# 요세푸스 문제
from collections import deque

n, k = map(int, input().split())
circle = deque(range(1, n+1))

result = []
for _ in range(n):
    circle.rotate(-(k-1))
    result.append(circle.popleft())

print("<" + str(result)[1:-1] + ">")