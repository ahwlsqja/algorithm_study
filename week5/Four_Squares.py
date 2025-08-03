# 어떤 수의 합을 이전 수들로 구성할 수 있지 않을까
# 루트 계산하는 방법: 2**(1/2)
'''
d[1] = 1^2
d[2] = 1^2 + 1^2
d[3] = 1^2 + 1^2 + 1^2
d[4] = 2^2
d[5] = 2^2 + 1^2
d[6] = 2^2 + 1^2 + 1^2
d[7] = 2^2 + 1^2 + 1^2 + 1^2
d[8] = 2^2 + 2^2
d[9] = 3^2
아이디어: 어떤 수 i에서 제곱수를 빼야한다. 근데 이떄 제곱수는 최대가 되어야함.
'''
'''
#시간초과
import sys
input = lambda: sys.stdin.readline().rstrip()

n = int(input())
d = [0] * (n+1)
a = 1
while(a**2 <= n):
    d[a**2] = 1
    a += 1

for i in range(1, n+1):
    if d[i] != 0:
        continue
    j = 1
    while(j*j <= i): #j제곱수를 최대한 i 이하 중 최대로 끌어올린다.
        if d[i] == 0:
            d[i] = d[j*j] + d[i-j*j]
        else:
            d[i] = min(d[i], d[j*j] + d[i-j*j])
        j += 1
print(d[n])
'''
#import math
import sys
input = lambda: sys.stdin.readline().rstrip()
n = int(input())
dp = [0] *(n+1)
dp[1] = 1

for i in range(2, n+1):
    min_calc = 50000
    for j in range(1, int(i**(1/2) + 1)):
        min_calc = min(min_calc, dp[i-j*j])
        #print(min_calc)
    dp[i] = min_calc + 1

    
print(dp[n])
                   




