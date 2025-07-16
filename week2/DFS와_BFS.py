from collections import deque

def dfs(graph, start, visited, result):
    visited[start] = True
    result.append(start)
    
    # 인접한 정점들을 번호 순으로 방문
    for neighbor in graph[start]:
        if not visited[neighbor]:
            dfs(graph, neighbor, visited, result)

def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True
    result = []
    
    while queue:
        node = queue.popleft()
        result.append(node)
        
        # 인접한 정점들을 번호 순으로 큐에 추가
        for neighbor in graph[node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)
    
    return result

# 입력 받기
n, m, v = map(int, input().split())

# 그래프 초기화 (인덱스 1부터 사용)
graph = [[] for _ in range(n + 1)]

# 간선 정보 입력
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# 각 정점의 인접 리스트를 정렬 (작은 번호부터 방문하기 위해)
for i in range(1, n + 1):
    graph[i].sort()

# DFS 수행
visited_dfs = [False] * (n + 1)
dfs_result = []
dfs(graph, v, visited_dfs, dfs_result)

# BFS 수행
visited_bfs = [False] * (n + 1)
bfs_result = bfs(graph, v, visited_bfs)

# 결과 출력
print(' '.join(map(str, dfs_result)))
print(' '.join(map(str, bfs_result)))