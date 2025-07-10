# 잃어버린 괄호
equation = input()
equation_lst = equation.split('-')

result = 0
first = sum(map(int, (equation_lst[0].split('+'))))
if equation[0] == '-': result -= first
else: result += first

for eq in equation_lst[1:]:
    val = sum(map(int, (eq.split('+'))))
    result -= val

print(result)