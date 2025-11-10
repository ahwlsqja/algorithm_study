import heapq
import sys
input = sys.stdin.readline
T = int(input())

for i in range(T):
    k = int(input()) #적용할 연산의 개수
    q_min = []
    q_max = []
    for j in range(k):
        s = input()
        if s == 'D 1':
            if len(q_max)==0:
                continue
            
            temp = heapq.heappop(q_max) #제거
            for k in q_min:
                q_min = []
                if k==temp:
                    continue
                heapq.heappush(q_min, k)
            
        elif s == 'D -1':
            if len(q_min)==0:
                continue
            
            temp = heapq.heappop(q_min) #제거
            print(q_min)
            for k in q_max:
                q_max = []
                if k==temp:
                    continue
                heapq.heappush(q_max, k)
                print(q_max)
            
        else:
            a = s.split()
            heapq.heappush(q_min, (int(a[1])))
            heapq.heappush(q_max, -(int(a[1])))
    print(q_max)
    if len(q_min) == 0 or len(q_max) == 0:
        print('EMPTY')
    else:
        print(-heapq.heappop(q_max), heapq.heappop(q_min))
        

