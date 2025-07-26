# 토마토 문제와 같은 흐름.
import sys
input = lambda: sys.stdin.readline().rstrip()
from collections import deque

N = int(input())
graph = []
for i in range(N):
    graph.append(list(map(int, input())))


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    home_count = 0
    q = deque()
    q.append((x, y))
    home_count += 1
    #시작점 방문 처리
    graph[x][y] = -1
    while(q):
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<N and 0<=ny<N and graph[nx][ny] == 1: #집이있는 범위?를 따지는것
                graph[nx][ny] = -1 #방문처리
                q.append((nx, ny))
                home_count += 1 #가정수
    
    return home_count #가정수
# 1개의 단지를 돌고, 거기에 속한 가정수도 개수를 센

count = 0 #단지수
home = []
for i in range(N):
    for j in range(N):
        if graph[i][j] == 1:
            home.append(bfs(i, j)) #집수
            count += 1 #단지수 

home.sort()
print(count)
for i in home:
    print(i)

