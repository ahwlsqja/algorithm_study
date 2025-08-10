N = int(input())

blocks = input()

#d[0] = 1 -> 0번째 블록까지의 에너지
#d[i] : i번째 블록까지의 에너지
dp = [1000000000] * N
dp[0] = 0
def check_prev(x):
    if x == 'B':
        return 'J'
    elif x== 'O':
        return 'B'
    elif x == 'J':
        return 'O'

for i in range(1, N):
    block = blocks[i]
    
    for j in range(i):
        prev = check_prev(blocks[i]) #여기서 실수함. 이전 블록을 확인하려면 check_prev(blocks[j])가 아니라 check_prev(blocks[i])를 해야한다!
        if blocks[j] == prev:
            dp[i] = min(dp[i], dp[j]+(i-j)*(i-j))


if dp[-1] == 1000000000:
    print(-1)
else:
    print(dp[-1])
        



    

