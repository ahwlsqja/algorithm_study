# 기타리스트
import sys

N, S, M = map(int, sys.stdin.readline().split())
v = list(map(int, sys.stdin.readline().split()))

dp = [[False]*(M+1) for _ in range(N+1)]
dp[0][S] = True

for i in range(N):
    for vol in range(M+1):
        if not dp[i][vol]: continue
        if vol + v[i] <= M:
            dp[i+1][vol + v[i]] = True
        if vol - v[i] >= 0:
            dp[i+1][vol - v[i]] = True

for vol in range(M, -1, -1):
    if dp[N][vol]:
        print(vol)
        break
else: print(-1)