def is_vps(s):
    stack = []

    pairs = {")": "("}

    for char in s:
        if char in '(':
            stack.append(char)

        elif char in ')':
            if not stack:
                return False

            if stack.pop() != pairs[char]:
                return False
    return len(stack) == 0

N = int(input())

for _ in range(N):
    line = input()

    if is_vps(line):
        print("YES")
    else:
        print("NO")