# 유기농 배추
import sys
sys.setrecursionlimit(10**6)

def dfs(x, y):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    visited[x][y] = True

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < m:
            if not visited[nx][ny] and graph[nx][ny] == 1:
                dfs(nx, ny)

t = int(sys.stdin.readline())

for i in range(t):
    m, n, k = map(int, sys.stdin.readline().split())

    graph = [[0] * m for _ in range(n)]
    visited = [[False] * m for _ in range(n)]
    for _ in range(k):
        x, y = map(int, sys.stdin.readline().split())
        graph[y][x] = 1

    cnt = 0
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1 and not visited[i][j]:
                dfs(i, j)
                cnt += 1
    print(cnt)