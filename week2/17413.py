S = input()
result = ''
stack = []
is_tag = False

for char in S:
    if char == '<':
        while stack:
            result += stack.pop()
        is_tag = True
        result += char
    elif char == '>':
        is_tag = False
        result += char
    elif is_tag:
        result += char
    elif char == ' ':
        while stack:
            result += stack.pop()
        result += char
    else:
        stack.append(char)

while stack:
    result += stack.pop()

print(result)
