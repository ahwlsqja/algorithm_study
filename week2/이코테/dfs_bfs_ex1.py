N, M = map(int, input().split())


def dfs(x, y):
    # 주어진 위치를 벗어났다면?
    if x<=-1 or x>=N or y <= -1 or y>=M:
        return False
    # 현재 노드를 아직 방문하지 않았다면
    if graph[x][y] == 0:
        graph[x][y] = 1 #방문처리를 해준다. 
        #상, 하, 좌, 우 위치도 재귀적으로 호출한다.
        #상하좌우 dfs는 return을 사용하지 않기 때문에
        # 단순히 연결된 노드에 대해서 방문처리를 수행하기 위한 목적. 
        dfs(x-1, y)
        dfs(x+1, y)
        dfs(x, y-1)
        dfs(x, y+1)
        return True
    return False #1을 마주쳤을때

graph = []
for i in range(N):
    graph.append(list(map(int, input())))

answer = 0
for i in range(N):
    for j in range(M):
        # 한번 수행되면 해당 노드와 연결된 모든 노드들도 방문처리할 수 있도록 하고
        # 시작점 노드가 처음 방문하는 것이라면 그때만 result 값을 증가시킨다. 
        if dfs(i, j) == True: #dfs가 가능하냐
            answer += 1


print(answer)



