'''
dfs로 접근할 경우 재귀 제한 1000이 있기 때문에 recursion error가 발생한다. 
sys.setrecursionlimit()을 통해 늘려주어야한다. 
'''
import sys
sys.setrecursionlimit(1000000)
input = lambda: sys.stdin.readline().strip()
N, M = map(int, input().split())
graph = []
sx = 0 #시작위치
sy = 0 #시작위치
for i in range(N):
    graph.append(list(input()))
    if "I" in graph[i]:
        for j in range(len(graph[i])):
            if graph[i][j] == 'I':
                sx = i
                sy = j
#상하좌우 이동
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def dfs(x, y): 
    count = 0 #만난사람 
    if graph[x][y] == 'P':
        count += 1
    graph[x][y] = 'X' #방문 처리
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if nx<0 or ny<0 or nx>=N or ny>=M:
            continue
        if graph[nx][ny] == 'X':
            continue
        else:
            count += dfs(nx, ny) #coutn 변수에 재귀호출결과 누적시키기     
    return count

answer = dfs(sx, sy)
if answer == 0:
    print("TT")
else:
    print(answer)
        
    

    