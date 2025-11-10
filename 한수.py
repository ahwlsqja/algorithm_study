from collections import deque

N = int(input())

q = deque(map(int, input().split()))

while(len(set(q)) != 2):
    