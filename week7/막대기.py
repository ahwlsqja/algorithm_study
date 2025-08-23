# 32
# 16 16 -> 안버림
# 8 8 16 -> 24 하나 버리기 -> 8 16
# 4 4 16 -> 안버림
# 2 2 4 4 16 -> 26 하나버리기 -> 2 4 4 16 -> 4 4 16 -> 2 2 4 16
#1 1 2 4 16 
#1 2 4 16 = 23 -> 4개
from collections import deque

X = int(input())
count = 0
sum_len = 0
q = deque()
q.append(64)
#[32]
#[32, 16, 8, 4]
#[16, 4, 2, 1]
while(sum_len != X):
    if sum(q) > X:
        now_len = min(q) // 2 #32 #16 #8 # 4
        while(sum(q)>X):
            q.pop()
        q.append(now_len)
    if sum(q) >= X:
        pass
    else:
        q.append(now_len)
    sum_len = sum(q)
    count = len(q)
    #print(sum_len)

print(count)

    