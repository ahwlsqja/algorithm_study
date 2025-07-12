from collections import deque
queue = deque()
N, M, V = map(int, input().split())
graph = [[] for _ in range(N+1)]
visited_dfs = [False] * (N + 1)
visited_bfs = [False] * (N + 1)
for i in range(M):
    v1, v2 = map(int,(input().split()))
    graph[v1].append(v2)
    graph[v2].append(v1)

for i in range(len(graph)):
    graph[i].sort()
def dfs(V):
    visited_dfs[V] = True
    print(V, end = ' ')
    for i in graph[V]:
        if visited_dfs[i] != True:
            dfs(i)
def bfs(V):
    queue.append(V)
    visited_bfs[V] = True
    while(queue):
        v = queue.popleft()
        print(v, end=" ")
        for i in graph[v]:
            if visited_bfs[i] != True:
                queue.append(i)
                visited_bfs[i] = True
dfs(V)
print()
bfs(V)

        