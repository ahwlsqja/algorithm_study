
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
    if i == 0:
        stack.append(nums[i])
        print(stack)
    else:    
        if flag == False:
            stack.append('-')
            stack.append('(')
            stack.append(nums[i])
            flag = True
            print(stack)
        else:
            stack.append(')')
            print(stack)
            
if flag== True:
    stack.append(')')
    print(stack)

s = ''
for i in (stack):
    i = re.sub(r'\b0+(\d+)', r'\1', i)
    s += i
print(stack)
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
'''