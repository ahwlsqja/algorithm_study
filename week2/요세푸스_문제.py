from collections import deque
N, K = map(int, input().split())
queue = deque()
for i in range(1, N+1):
    queue.append(i)
print("<", end = '')
answer = []
while(True):
    if len(queue) == 0:
        break
    for i in range(K):
        if i < K-1:
            queue.append(queue.popleft())
        else:
            answer.append(queue.popleft())

for i in range(len(answer)):
    if i == len(answer)-1:
        print(answer[i], end = '>')
    else:
        print(answer[i], end = ', ')