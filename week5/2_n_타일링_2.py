#중복되는 경우를 잘 생각해야한다. 

n = int(input())
'''
#이 부분을 여기 넣으면 n이 2보다 작으면 index error가 날 수 있다. 
d = [0] * (n+1)
d[1] = 1
d[2] = 3
'''
if n == 1: #예외 경우 주의
    print(1)
else:
    d = [0] * (n+1)
    d[1] = 1
    d[2] = 3
    for i in range(3, n+1):
        d[i] = d[i-1] + (2* d[i-2])

    print(d[n] % 10007)