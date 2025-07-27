'''
import sys
input = lambda: sys.stdin.readline().rstrip()
N = int(input())
ls = list(map(int, input().split()))
M = int(input())

if sum(ls) <= M:
    print(max(ls))

else:
    ls.sort()
    
    mid = M // len(ls)
    
    buget_sum = 0
    a = mid
    index = 0
    for i in range(len(ls)):
        if ls[i] <= mid:
            buget_sum += ls[i]
        else:
            index = i
            
      
    while(True): #buget_sum이 M보다 커지면 break
        buget_sum = buget_sum + (a * (len(ls)-index+1))
        if buget_sum > M:
            break
        buget_sum = buget_sum - (a * (len(ls)-index+1))
        a+=1

    print(a-1)
'''

import sys
input = lambda: sys.stdin.readline().rstrip()
N = int(input())
ls = list(map(int, input().split()))
M = int(input())

if sum(ls) <= M:
    print(max(ls))

else:
    ls.sort()
    
    def buget_valid(limit):
        total = 0
        for i in ls:
            total += min(i, limit)
        return total<=M
    
    left, right = 0, max(ls)
    answer = 0 #정답이 되는 limit값            
    
    #이진탐색 시작
    while(left <= right): #buget_sum이 M보다 커지면 break
        mid = (left+right)//2
        if buget_valid(mid): #mid를 상한가로 했을 때 M예산보다 작거나 같나요?
            answer = mid #정답 갱신
            left = mid + 1 #mid를 상한가로 하면 범위 안에 total이 있으므로 mid보다 큰 값 위주로 탐색해보자.
        else:
            right = mid - 1
        
    print(answer)

