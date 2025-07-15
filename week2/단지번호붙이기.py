from collections import deque

def solution_dfs():
    n = int(input())
    grid = []
    for _ in range(n):
        row = input()
        grid.append([int(c) for c in row])
    
    visited = [[False] * n for _ in range(n)]
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    def dfs(x, y):
        visited[x][y] = True
        count = 1
        
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if (0 <= nx < n and 0 <= ny < n and 
                grid[nx][ny] == 1 and not visited[nx][ny]):
                count += dfs(nx, ny)
        
        return count
    
    complexes = []
    
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 1 and not visited[i][j]:
                house_count = dfs(i, j)
                complexes.append(house_count)
    
    print(len(complexes))
    complexes.sort()
    for count in complexes:
        print(count)

solution_dfs()  # DFS 방식