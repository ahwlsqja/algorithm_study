import sys
input = lambda: sys.stdin.readline().rstrip()
M, N = map(int, input().split())
graph = []
from collections import deque
for i in range(N):
    graph.append(list(map(int, input().split())))
q = deque()
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for i in range(N):
    for j in range(M):
        if graph[i][j] == 1:
            q.append((i, j))
def bfs():    
    while(q):
        sx, sy = q.popleft() #익은토마토 하나를 꺼냄.
        
        for i in range(4):#익은토마토에서 상하좌우 이동
            nx = sx + dx[i]
            ny = sy + dy[i]
            if 0<= nx < N and 0<= ny <M and graph[nx][ny] == 0: #다음 위치(안익은 곳)가 범위 안에 있으면
                graph[nx][ny] = graph[sx][sy]  + 1 #날짜수 더해주기
                q.append((nx, ny))
            
answer = 0
bfs()
for i in range(N):
    for j in range(M):
        if graph[i][j] == 0: #안익은 곳 발견?
            print(-1)
            exit(0) #break말고 exit(0)을 써줌.
    answer = max(answer, max(graph[i]))


print(answer - 1) # 1부터 세었으므로 최소 날짜는 1뺴주어야함.
            
