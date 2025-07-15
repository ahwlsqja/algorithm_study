DFS와 BFS는 대표적인 그래프 탐색 알고리즘이다. 
# 그래프 알고리즘
위키독스에서 그래프 알고리즘을 설명하기 위한 예시가 있어 가져와보았다. 
> 우리집에서 학교까지의 거리가 가까운지, 친구 집에서 학교까지가 가까운지 알고싶다. 그렇다면 **각 집들과 학교를 어떻게 표현**할 지 알아야 한다.
그 다음 우리 집에서 학교까지 갈 수 있는지, 학교에서 친구 집까지 갈 수 있는지 알아야한다.
갈 수 있다면? **최단경로**는 어떻게 되는지, **길의 연결이 끊기면 다른 길은 없는지** 등을 알아보는 것이 그래프 알고리즘이다. 

### 그래프 알고리즘의 분류
그래프 알고리즘을 통해 배울 수 있는 알고리즘의 종류에 대해서 알아놓자. 
다양한 명칭이 나와서 간혹 헷갈렸는데, 이번 기회에 확실히 알고 넘어가자.

#### 탐색 알고리즘
그래프를 탐색하기 위해 각 정점들의 연결을 알 수 있다. 
대표적으로 DFS(깊이 우선 탐색)과 BFS(너비 우선 탐색) 이 있다. 

- 탐색(Search)이란?
많은 양의 데이터 중에서 원하는 데이터를 찾는 과정이다.

#### 최단 경로 알고리즘
연결이 되는 것을 확인했다면 두 정점의 최단 경로를 알고 싶다. 
대표적으로 
- 다익스트라 알고리즘
- 벨만 포드 알고리즘
- 플로이드 와샬 알고리즘

#### 최소 신장 트리
최단 경로 알고리즘이 두 정점을 대상으로 했다면 최소 신장 트리는** 모든 정점을 연결하는 최단경로**라고 생각하면 된다.
- 각각 거리는 최단 경로가 아닐 수 있는데, **모든 경로를 지나는 최소값**을 구하는 것이다. 
대표적으로
- 쿠르스칼 알고리즘
- 프림 알고리즘

# 탐색 알고리즘
앞서 설명한 탐색알고리즘 DFS, BFS에 대해서 알아보자. 
그 전에 반드시 알아야할 두가지 자료구조에 대해 알아보자.
## 스택 자료구조
- 먼저 들어온 데이터가 나중에 나가는 형식(선입후출, FILO)
- 입구와 출구가 동일하다. 
![박스쌓기 예시](https://velog.velcdn.com/images/owlemily/post/5c167f12-c7e2-4a99-9275-50f2f24bc208/image.png)
- 삽입과 삭제 연산이 있다. 
파이썬에서 스택 구조를 이용하기 위해서는 `리스트` 자료형을 이용하면 된다.
- `append()`와 `pop()`의 시간복잡도는 O(1)이므로 사용하기 적합하다.
```python
stack = []

# 삽입(5) - 삽입(2) - 삽입(3) - 삽입(7) - 삭제() - 삽입(1) - 삽입(4) - 삭제()
stack.append(5)
stack.append(2)
stack.append(3)
stack.append(7)
stack.pop()
stack.append(1)
stack.append(4)
stack.pop()

print(stack) # 최하단 원소부터 출력 #[5, 2, 3, 1]
print(stack[::-1]) # 최상단 원소부터 출력 #[1, 3, 2, 5]
```
- ~~최상단 원소부터 출력하는 것이 간혹 헷갈린다.~~

## 큐 자료구조
- 먼저 들어온 데이터가 먼저 나가는 형식(선입선출, FIFO)
- 입구와 출구가 모두 뚫려있는 터널과 같은 형태
- 대기열 - 차례대로 먼저 들어온 데이터가 먼저 처리됨.

```python
from collections import deque 

# 큐(Queue) 구현을 위해 deque 라이브러리 사용
queue = deque()

# 삽입(5) - 삽입(2) - 삽입(3) - 삽입(7) - 삭제() - 삽입(1) - 삽입(4) - 삭제()
queue.append(5)
queue.append(2)
queue.append(3)
queue.append(7)
queue.popleft() #가장 왼쪽의 데이터를 꺼내기
queue.append(1)
queue.append(4)
queue.popleft()

print(queue) # 먼저 들어온 순서대로 출력 #[3, 7, 1, 4]
queue.reverse() # 다음 출력을 위해 역순으로 바꾸기
print(queue) # 나중에 들어온 원소부터 출력 #[4, 1, 7, 3]
```
- 리스트 자료형을 이용해서 큐를 구현할 수도 있다. 기능적으로는 가능하지만 시간복잡도가 더 높다. 
그 이유는 맨 앞의 원소를 제거할 때 시간복잡도가 O(K)이기 때문이다. 

> 리스트는 내부적으로 연속된 메모리 공간을 사용한다. 
append()를 통해 뒤에 원소를 추가하고 pop(0)을 통해 리스트의 앞 원소를 제거할 수 있다. 리스트의 맨 앞의 값을 꺼내면 그 뒤의 모든 원소를 앞으로 한칸씩 밀어야한다. 따라서 시간복잡도는 **O(K)**이다.

> 파이썬의 collections.deque는 양방향 연결 리스트 기반이라서 append(), popleft() 모두 O(1)의 시간복잡도를 가진다. 
앞에서 꺼내도 위치를 밀 필요가 없어서 시간복잡도가 더 낮고 효율적으로 동작한다. 

## 재귀함수(Recursive Function)
- 자기 자신을 다시 호출하는 함수
```python
def recursive_function():
    print('재귀 함수를 호출합니다.')
    recursive_function()

recursive_function()
```
- '재귀 함수를 호출합니다.'라는 문자열을 무한히 출력한다.
- 어느 정도 출력하다가 최대 재귀 깊이 초과 메세지가 출력된다. 파이썬에서는 오류메세지가 출력되고 자동으로 프로그램이 종료된다.
![](https://velog.velcdn.com/images/owlemily/post/4638247b-20ee-48b5-8a81-1049e82821e2/image.png)
- 컴퓨터 시스템 상에서 함수가 재귀적으로 호출되면 컴퓨터 시스템의 스택 프레임에 이러한 함수가 반복적으로 쌓여서 가장 마지막으로 호출된 함수가 처리가 된 이후에 그 함수를 불렀던 함수까지 처리가 되는 방식이다. 
>-> 스택 자료구조 안에 함수의 정보가 차례로 담겨서 컴퓨터 메모리에 올라간다. 
-> 컴퓨터 메모리는 한정된 자원이기 때문에 무작정 함수가 종료되지 않고 계속 쌓아 올려서 재귀적으로 호출만하면 빠르게 메모리가 차서 문제가 발생할 수 있어 재귀의 깊이를 제한해둔 것이다.
- 재귀 함수를 문제 풀이에 사용할 경우 **종료조건**을 반드시 명시해야한다.
종료조건을 제대로 명시하지 않으면 함수가 무한히 호출될 수 있다.
```python
# 종료조건 : i == 100인 경우 종료
def recursive_function(i):
    # 100번째 호출을 했을 때 종료되도록 종료 조건 명시
    if i == 100:
        return
    print(i, '번째 재귀함수에서', i + 1, '번째 재귀함수를 호출합니다.')
    recursive_function(i + 1)
    print(i, '번째 재귀함수를 종료합니다.')

recursive_function(1)
```
- 재귀 함수를 이용하면 스택에 데이터를 넣었다가 꺼내는 것과 마찬가지고 차례로 호출되었다가 마지막의 함수가 종료되며 차례로 종료된다.
### 재귀 함수 예제
#### 최대공약수 계산(유클리드 호제법) 예제
![](https://velog.velcdn.com/images/owlemily/post/840a426f-2ab6-4c22-a30b-12cc30e6a2fd/image.png)
```python
def gcd(a, b):
	if a % b == 0:
    	return b
    else:
    	return gcd(b, a%b)
print(gcd(192, 162))
```
### 재귀 함수 사용 시 유의사항
- 재귀함수를 잘 활용하면 복잡한 알고리즘을 간결하게 작성할 수 있다.
이때, 오히려 이해하기 어려운 형태의 코드가 될 수도 있으므로 신중해야한다.
- 모든 재귀함수는 반복문을 이용해서 동일한 기능을 구현할 수 있다.
- 재귀함수가 반복문보다 유리한 경우도 있고 불리한 경우도 있다. 
- 컴퓨터가 함수를 연속적으로 호출하면 컴퓨터 메모리 내부의 스택프레임에 쌓인다. 따라서 스택을 사용해야할 때 구현상 스택 라이브러리 대신에 재귀함수를 이용하는 경우가 많다.

## DFS(Depth-First Search)
- 깊이 우선 탐색, 깊은 부분을 우선적으로 탐색하는 알고리즘
- DFS는 **스택 자료구조(혹은 재귀함수)**를 이용하며, 구체적인 동작 과정은 다음과 같다. 
> 1. 탐색 시작 노드를 스택에 삽입하고 방문처리를 한다.
2. 스택의 최상단 노드에 방문하지 않은 인접한 노드가 하나라도 있으면 그 노드를 스택에 넣고 방문 처리한다. 방문하지 않은 인접 노드가 없으면 스택에서 최상단 노드를 꺼낸다.
3. 더 이상 2번의 과정을 수행할 수 없을 때까지 반복한다.

```python
# DFS 함수 정의
def dfs(graph, v, visited):
    # 현재 노드를 방문 처리
    visited[v] = True
    print(v, end=' ')
    # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

# 각 노드가 연결된 정보를 리스트 자료형으로 표현(2차원 리스트)
graph = [
  [],
  [2, 3, 8],
  [1, 7],
  [1, 4, 5],
  [3, 5],
  [3, 4],
  [7],
  [2, 6, 8],
  [1, 7]
]

# 각 노드가 방문된 정보를 리스트 자료형으로 표현(1차원 리스트)
visited = [False] * 9

# 정의된 DFS 함수 호출
dfs(graph, 1, visited)
```
- 그래프에서 인덱스 0은 사용하지 않고, 직관적으로 노드의 번호와 인덱스를 1부터 일치시켜준다.
## BFS(Breadth-First Search)
- 너비우선탐색, 그래프에서 가까운 노드부터 우선적으로 탐색하는 알고리즘이다.
- BFS는 **큐 자료구조**를 이용하며 구체적인 동작 과정은 다음과 같다. 
>1. 탐색 시작 노드를 큐에 삽입하고 방문처리를 한다.
2. 큐에서 노드를 꺼낸 뒤에 해당 노드의 인접 노드 중에서 방문하지 않은 노드를 모두 큐에 삽입하고 방문처리한다.
3. 더 이상 2번의 과정을 수행할 수 없을 때까지 반복한다.

```python
from collections import deque

# BFS 함수 정의
def bfs(graph, start, visited):
    # 큐(Queue) 구현을 위해 deque 라이브러리 사용
    queue = deque([start])
    # 현재 노드를 방문 처리
    visited[start] = True
    # 큐가 빌 때까지 반복
    while queue:
        # 큐에서 하나의 원소를 뽑아 출력
        v = queue.popleft()
        print(v, end=' ')
        # 해당 원소와 연결된, 아직 방문하지 않은 원소들을 큐에 삽입
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

# 각 노드가 연결된 정보를 리스트 자료형으로 표현(2차원 리스트)
graph = [
  [],
  [2, 3, 8],
  [1, 7],
  [1, 4, 5],
  [3, 5],
  [3, 4],
  [7],
  [2, 6, 8],
  [1, 7]
]

# 각 노드가 방문된 정보를 리스트 자료형으로 표현(1차원 리스트)
visited = [False] * 9

# 정의된 BFS 함수 호출
bfs(graph, 1, visited)
```
## 예제 - <문제1>
![](https://velog.velcdn.com/images/owlemily/post/8fa57693-9a23-4feb-b5fc-d2387263b9e3/image.png)
- 연결요소 찾기(connected component)를 푸는 문제라고도 볼 수 있다. 
![](https://velog.velcdn.com/images/owlemily/post/101cb7ea-ed00-4d42-b6f5-c95347d52705/image.png)
- 상하좌우 인접한 노드를 그래프 형태로 표현
- 특정 지점에서 dfs/bfs를 수행해서 이동가능한 경우 방문처리를 한다. 
- 본 코드에서 dfs/bfs가 한번 전체 다 이루어지면 연결요소가 1개 있는 것이다.
![](https://velog.velcdn.com/images/owlemily/post/09f465b0-fb78-40d3-bd25-5185edbde51b/image.png)
```python
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
        return True #연결 덩어리 하나 탐색 완료
    return False #1을 마주쳤을때

graph = []
for i in range(N):
    graph.append(list(map(int, input()))) #한 글자씩 잘라서 정수(int)로 바꿔주는 것

answer = 0
for i in range(N):
    for j in range(M):
        # 한번 수행되면 해당 노드와 연결된 모든 노드들도 방문처리할 수 있도록 하고
        # 시작점 노드가 처음 방문하는 것이라면 그때만 result 값을 증가시킨다. 
        if dfs(i, j) == True: #dfs가 가능하냐 #True라는 것은 해당 위치에서 덩어리 하나 발견했다는 뜻
            answer += 1


print(answer)
```
## 예제 - <문제2>
![](https://velog.velcdn.com/images/owlemily/post/0c4a5572-5f9c-4c78-a357-e8a2da7dbc50/image.png)
![](https://velog.velcdn.com/images/owlemily/post/3854c6af-7a1a-4ab5-acb3-8223d1bfa1a4/image.png)
#### 문제 해결 아이디어
- BFS는 시작지점에서 가까운 노드부터 차례대로 그래프의 모든 노드를 탐색한다.
- 상하좌우로 연결된 모든 노드로의 거리가 1로 동일하다.
```python
from collections import deque

N, M = map(int, input().split())
graph = []
for i in range(N):
    graph.append(list(map(int, input())))

#상하좌우
dx = [-1, 1, 0, 0] 
dy = [0, 0, 1, -1]

def bfs(x, y): #시작하는 위치를 넣어줌
    queue = deque()
    queue.append((x, y))
    while(queue):
        x, y = queue.popleft()
        # x, y에서 상하좌우 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= N or ny >= M:
                continue
            if graph[nx][ny] == 0:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))
    return graph[N-1][M-1]
print(bfs(0, 0))
```
- graph[x][y]에 이동한 칸 수를 누적하여 더한 후 (N, M)에 도달하였을 때 저장한 칸 수를 반환한다.

> **참고**
현재 참여하고 있는 코딩테스트 스터디 깃헙 링크입니다^^
https://github.com/ahwlsqja/algorithm_study
**기타**
https://wikidocs.net/206316