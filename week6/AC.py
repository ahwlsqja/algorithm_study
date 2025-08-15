import sys
input = lambda: sys.stdin.readline().rstrip()
from collections import deque

T = int(input())


# D가 짝수면 deque에서 앞부분을 빼고, D가 홀수면 deque에서 뒷부분을 빼면 된다. 
for _ in range(T):
    p = input()
    n = int(input())
    ls_nums = input()[1:-1]
    if n==0:
        deq = deque()
    else:
        deq = deque(map(int, ls_nums.split(',')))
    r_count = 0
    flag = False
    for i in range(len(p)):
        if p[i] == "R":
            r_count += 1
        elif p[i] == "D":
            if len(deq)<1:
                print("error")
                flag = True
                break
            elif r_count % 2==0:
                deq.popleft()
            elif r_count % 2 != 0:
                deq.pop()
    if r_count % 2 == 0 and flag == False:
            print('['+','.join(map(str, deq))+']')
    elif r_count % 2 != 0 and flag == False:
        print('['+','.join(map(str, reversed(deq)))+']')


    

    



