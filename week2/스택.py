import sys
input = lambda: sys.stdin.readline().rstrip()
N = int(input())
stack = []
for i in range(N):
    s = list(input().split())
    if "push" in s[0]:
        stack.append(s[-1])
    elif "pop" in s:
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop())
    elif "size" in s[0]:
        print(len(stack))
    elif "empty" in s[0]:
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    elif "top" in s[0]:
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])
