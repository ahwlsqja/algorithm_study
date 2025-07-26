N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
for i in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)

# 서로서로에게 연결되는 경우의 수를 모두 구한 뒤에 최소값의 인덱스(사람번호)를 구해야함.

