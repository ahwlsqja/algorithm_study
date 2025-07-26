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