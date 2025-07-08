'''
import re
import sys
input = lambda: sys.stdin.readline().rstrip()
s = input()
nums = s.split('-')
#nums = nums.split('-')
#print(nums)
stack = []
flag = False # 괄호가 열렸는지 확인
for i in range(len(nums)):
    if '+' not in nums[i]:
        stack.append(nums[i])
        
        if flag == False:
            stack.append('-')
            stack.append('(')
            flag = True
        else:
            stack.append(')')
            
    else:
        stack.append(nums[i])
        if flag == True:
            stack.append(')')
s = ''
for i in (stack):
    i = re.sub(r'\b0+(\d+)', r'\1', i)
    s += i
answer = eval(s)

print(answer)
'''

import re
import sys

input = lambda: sys.stdin.readline().rstrip()
s = input()
# 0 제거
s = re.sub(r'\b0+(\d+)', r'\1', s)

# 첫 '-' 기준으로 split
parts = s.split('-')
# 첫 부분은 괄호 없이 더함
total = sum(map(int, parts[0].split('+')))
# 나머지는 모두 괄호로 묶어서 더한 뒤 빼기
for part in parts[1:]:
    total -= sum(map(int, part.split('+')))
print(total)