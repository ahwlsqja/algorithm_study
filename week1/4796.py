# 캠핑
import sys

cnt = 1
while True:
    line = sys.stdin.readline()
    l, p, v = map(int, line.strip().split())
    if l == 0 and p == 0 and v == 0: break

    result = (v // p * l) + min(v % p, l)
    print(f'Case {cnt}: {result}')
    cnt += 1