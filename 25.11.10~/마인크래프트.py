N, M, B = map(int, input().split())

cnt = [0] * 257
for _ in range(N):
    for h in map(int, input().split()):
        cnt[h] += 1

heights = [h for h in range(257) if cnt[h] > 0]
min_h, max_h = heights[0], heights[-1]

best_time = 10**18
best_h = 0

for h in range(min_h, max_h+1): #목표높이
    remove = 0 #깎는 블록수
    plant = 0 #심는 블록수
    for i in range (min_h, max_h+1): #현재 땅의 높이값
        c = cnt[i] #이 높이값을 가진 칸 수
        if c == 0:
            continue
        if i > h : #현재 고려하는 땅의 높이가 목표 높이보다 크다면
            remove += (i - h) * c 
        elif i < h:
            plant += (h-i) * c
    #인벤토리 개수 확인
    if remove + B < plant: # 깎아서 얻는 블록 + 초기보유블록 < 채우는데 필요한 블록
        continue
    t = remove * 2 + plant
    if t < best_time:
        best_time = t
        best_h = h

print(best_time, best_h)

'''
import sys
input = sys.stdin.readline

N, M, B = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]

min_h = min(min(row) for row in grid)
max_h = max(max(row) for row in grid)

best_time = 10**18
best_h = -1

for h in range(max_h, min_h - 1, -1):  # 높은 h부터
    remove_blocks = 0
    place_blocks = 0

    for r in range(N):
        for c in range(M):
            cur = grid[r][c]
            if cur > h:
                remove_blocks += cur - h
            elif cur < h:
                place_blocks += h - cur

    if remove_blocks + B < place_blocks:
        continue

    t = remove_blocks * 2 + place_blocks
    if t < best_time:
        best_time = t
        best_h = h

print(best_time, best_h)

'''


