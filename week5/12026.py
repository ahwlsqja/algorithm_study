# BOJ 거리
import sys

INF = 10**18

n = int(sys.stdin.readline().strip())
s = sys.stdin.readline().strip()

def next_char(c):
    if c == 'B': return 'O'
    if c == 'O': return 'J'
    return 'B'

dp = [INF] * n
dp[0] = 0

for i in range(n):
    if dp[i] == INF:
        continue
    need = next_char(s[i])
    for j in range(i + 1, n):
        if s[j] == need:
            cost = (j - i) ** 2
            if dp[j] > dp[i] + cost:
                dp[j] = dp[i] + cost

print(-1 if dp[n-1] == INF else dp[n-1])