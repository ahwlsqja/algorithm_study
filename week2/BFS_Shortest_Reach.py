from collections import deque
q = int(input())
def bfs(s, distance, queue):
    queue.append(s)
    distance[s] = 0 #시작 정점은 거리 0
    while(queue):
        visit = queue.popleft()
        for i in graph[visit]:
            if distance[i] == -1:
                distance[i] = distance[visit] + 6 #거리는 이전 노드 방문 거리에 6을 더하기
                queue.append(i)  
    return distance
for i in range(q):
    n, m = map(int, input().split())
    distance = [-1] * (n+1) #거리 저장 #방문 안함으로 초기화
    queue = deque()

    graph = [[] for _ in range(n+1)] #노드 개수만큼 graph만들기
    for j in range(m):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)
    s = int(input())
    answer = bfs(s, distance, queue)
    for k in range(len(answer)):
        if k == 0 or k == s:
            continue
        if answer[k] == 0:
            print(-1, end =" ")
        else:
            print(answer[k], end = " ")
    print()

