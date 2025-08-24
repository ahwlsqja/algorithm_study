#  파티
import sys
import heapq

input = sys.stdin.readline
INF = 10**15

def dijkstra(start, graph, n):
    dist = [INF] * (n + 1)
    dist[start] = 0
    pq = [(0, start)]
    while pq:
        d, u = heapq.heappop(pq)
        if d != dist[u]: continue
        for v, w in graph[u]:
            nd = d + w
            if nd < dist[v]:
                dist[v] = nd
                heapq.heappush(pq, (nd, v))
    return dist

N, M, X = map(int, input().split())
graph = [[] for _ in range(N + 1)]
rev_graph = [[] for _ in range(N + 1)]

for _ in range(M):
    a, b, t = map(int, input().split())
    graph[a].append((b, t))
    rev_graph[b].append((a, t))

dist_from_X = dijkstra(X, graph, N)
dist_to_X = dijkstra(X, rev_graph, N)

ans = 0
for i in range(1, N + 1):
    if dist_from_X[i] >= INF or dist_to_X[i] >= INF: continue
    ans = max(ans, dist_from_X[i] + dist_to_X[i])

print(ans)