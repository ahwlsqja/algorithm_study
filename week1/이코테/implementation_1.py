N = int(input())
plan = list(input().split())

#L, R, U, D
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
x = 1
y = 1

for i in range(len(plan)):
    if plan[i] == 'L':
        nx = x + dx[0]
        ny = y + dy[0]
    elif plan[i] == 'R':
        nx = x + dx[1]
        ny = y + dy[1]
    elif plan[i] == 'U':
        nx = x + dx[2]
        ny = y + dy[2]
    else:
        nx = x + dx[3]
        ny = y + dy[3]
    
    if nx <= N and ny <= N and nx >= 1 and ny >= 1: #범위내에 있다면 현재 위치(x, y) 바꿔주기
        x = nx
        y = ny

print(x, y)
