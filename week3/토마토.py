import sys
input = lambda: sys.stdin.readline().rstrip()
from collections import deque

M, N, H = map(int, input().split())
#M은 가로
#N은 세로
#H는 쌓은 상자의 수

graph = []
for h in range(H):
    NM = []
    for n in range(N):
        NM.append(list(map(int, input().split())))
    graph.append(NM)

#위, 아래, 왼쪽, 오른쪽, 앞, 뒤
move = [(-1, 0, 0), (1, 0, 0), (0, -1, 0), (0, 1, 0), (0, 0, 1), (0, 0, -1)]

#익는 연결요소 돌기
#하루가 지나면 연결된 곳들 다 익음
#1인 칸에서 시작해야함.
def bfs():
    q = deque()
    for i in range(H):
        for j in range(N):
            for k in range(M):
                if graph[i][j][k] == 1:
                    q.append((i, j, k))
    
    while(q):
        z, x, y = q.popleft()
        for m in move:
            nx = x + m[0]
            ny = y + m[1]
            nz = z + m[2]
            
            if 0<=nx<N and 0<=ny<M and 0<=nz<H and graph[nz][nx][ny]==0:
                q.append((nz, nx, ny))
                graph[nz][nx][ny] = graph[z][x][y] +1





bfs()
answer = 0
for i in range(H):
    for j in range(N):
        for k in range(M):
            if graph[i][j][k] == 0: #안익은 칸이 있으면
                print(-1)
                exit(0)
            else:
                answer = max(answer, graph[i][j][k] -1)

print(answer)
