import sys
import heapq

input = sys.stdin.readline
q = []
N = int(input())
for i in range(N):
    x = int(input())
    if x == 0:
        if len(q) == 0:
            print(0)
        else:
            print(heapq.heappop(q)[1])
    else:
        heapq.heappush(q, (abs(x), x))
