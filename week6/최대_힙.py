import heapq
import sys
input = sys.stdin.readline
N = int(input())
q = []
for i in range(N):
    x = int(input())
    if x == 0:
        if len(q) == 0:
            print(0)
        else:
            print(-(heapq.heappop(q)))
    else:
        heapq.heappush(q, -x)