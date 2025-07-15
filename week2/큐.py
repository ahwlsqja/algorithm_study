import sys
input = lambda: sys.stdin.readline().rstrip()
from collections import deque
queue = deque()
N = int(input())
for i in range(N):
    s = list(input().split())
    if "push" in s[0]:
        queue.append(s[1])
    elif "pop" in s:
        if not queue:
            print(-1)
        else:
            print(queue.popleft())
    elif "size" in s:
        print(len(queue))
    elif "empty" in s:
        if not queue:
            print(1)
        else:
            print(0)
    elif "front" in s:
        if not queue:
            print(-1)
        else:
            print(queue[0])
    elif "back" in s:
        if not queue:
            print(-1)
        else:
            print(queue[-1])
    