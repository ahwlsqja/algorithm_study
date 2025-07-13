# 스택
import sys
n = int(sys.stdin.readline())

stack = []
for i in range(n):
    code = sys.stdin.readline()
    start = code[:2]
    if start == 'pu':
        v = int(code.split()[1])
        stack.append(v)
    if start == 'po':
        if len(stack) == 0: print(-1)
        else:
            v = stack.pop()
            print(v)
    if start == 'si':
        print(len(stack))
    if start == 'em':
        print(int(len(stack) == 0))
    if start == 'to':
        if len(stack) == 0: print(-1)
        else: print(stack[-1])