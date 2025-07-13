# 큐
from collections import deque
import sys

n = int(sys.stdin.readline())

queue = deque()
for _ in range(n):
    code = sys.stdin.readline()
    start = code[:2]
    if start == 'pu':
        v = int(code.split()[1])
        queue.append(v)
    if start == 'po':
        if len(queue) == 0: print(-1)
        else:
            v = queue.popleft()
            print(v)
    if start == 'si':
        print(len(queue))
    if start == 'em':
        print(int(len(queue) == 0))
    if start == 'fr':
        if len(queue) == 0: print(-1)
        else: print(queue[0])
    if start == 'ba':
        if len(queue) == 0: print(-1)
        else: print(queue[-1])