import sys
from collections import deque
input = lambda: sys.stdin.readline().rstrip()
N, M, K = map(int, input().split())

# 연결요소의 개수를 구해서 가장 큰 개수를 출력하면 되지 않을까
graph = [[0] * M for _ in range(N)]
for k in range(K):
    r,c = map(int, input().split())
    graph[r-1][c-1] = 1

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


visited = [[0] * M for _ in range(N)]

def bfs(i, j):
    q = deque()
    q.append((i, j))
    count_max = 0
    while(q):
        x, y = q.popleft()
        count_max += 1
        visited[x][y] = 1 #방문 처리
        for i in range(4): #상하좌우 확인
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<N and 0<=ny<M and visited[nx][ny] == 0 and graph[nx][ny] == 1: #방문하지 않고, 범위 내에 있고, 칸 수가 1인 경우 
                q.append((nx, ny))
                visited[nx][ny] = 1 #방문 처리
    return count_max


answer = 0
for i in range(N):
    for j in range(M):
        if graph[i][j] == 1:
            count = bfs(i,j)
            answer = max(answer, count) #칸에 적힌 수가 제일 큰 것

print(answer)

