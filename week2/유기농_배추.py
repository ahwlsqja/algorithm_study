'''
가로 세로 x, y가 헷갈렸던 문제
'''
import sys
input = lambda: sys.stdin.readline().rstrip()
sys.setrecursionlimit(1000000)
T = int(input())

def dfs(x, y):
    if x<0 or y<0 or x>=N or y>=M:
        return False
    if graph[x][y] == 1:
        graph[x][y] = 0 #방문표시
        dfs(x+1, y)
        dfs(x-1, y)
        dfs(x, y+1)
        dfs(x, y-1)
        return True
    return False


for i in range(T):
    M, N, K = map(int, input().split())

    graph = [[0] * (M) for _ in range(N)]

    for j in range(K):
        x, y = map(int, input().split())
        graph[y][x] = 1 #x: 가로 y:세로
    answer = 0
    for k in range(N):
        for h in range(M):
            if dfs(k, h) == True:
                answer += 1

                
    print(answer)
    



