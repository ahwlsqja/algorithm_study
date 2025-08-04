N, r, c = map(int, input().split())
#2x2씩 반복해야하기때문에 N = 3 -> 2^3 x 2^3 = 64 / 4 = 16개의 2x2를 반복

answer = 0
while N != 0:
    N -= 1
    size = 2**N

    