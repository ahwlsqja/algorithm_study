s = input()
count = 0 #이동할 수 있는 경우의 수

dx = [1, -1, 1, -1, 2, 2, -2, -2]
dy = [2, 2, -2, -2, 1, -1, 1, -1]

y = (ord(s[0]) - ord('a')) + 1 # 1을 더해주는 것을 주의 (1, 2, 3, 4..., 8)
x = int(s[1])
for i in range(len(dx)):
    nx = x + dx[i]
    ny = y + dy[i]
    if ny > 8 or ny < 1 or nx < 1 or nx > 8:
        continue
    else:
        count += 1

print(count)