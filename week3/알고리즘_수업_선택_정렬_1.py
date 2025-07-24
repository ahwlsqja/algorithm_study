'''
# 뒤의 인덱스부터 정렬해나가기 시작. 
# 시간초과 발생한 코드. 함수를 사용하지 않으면 최적화가 안됨.
import sys
input = lambda: sys.stdin.readline().rstrip()
N, K = map(int, input().split())
nums = []
nums = list(map(int, input().split()))
count = 0
for i in range(len(nums)-1, 0, -1):
    max_index = i
    max_val = nums[i]
    for j in range(i-1, -1, -1): #작은 인덱스부터 해도됨
        if max_val < nums[j]:
            max_index = j
            max_val = nums[j]
    if i != max_index: #같지 않을 때 스왑
        a, b = nums[i], nums[max_index]
        nums[i], nums[max_index] = b, a
        count += 1
    if count == K:
        print(a, b)
        exit(0)
        
print(-1)
'''

#선택정렬 알고리즘으로 시간초과 해결
import sys
input = lambda: sys.stdin.readline().rstrip()
N, K = map(int, input().split())
nums = []
nums = list(map(int, input().split()))
#선택정렬 함수
def selection_sort(N):
    cnt = 0    
    for i in range(N-1, 0, -1):
        last = i
        for j in range(i-1, -1, -1):
            if (nums[j] > nums[last]):
                last = j        
        if last != i:
            #리스트 값 스왑
            nums[i], nums[last] = nums[last], nums[i]
            cnt += 1
        if (cnt == K):            
            return (print(nums[last], nums[i]))
    return(print(-1))
#선택정렬 함수 호출
selection_sort(N)
