'''
1
1
1
2 = 1+1
2 = 1+1
3 = 1+2
4 = 1+3
5 = 1+ 4
7 = 4+3
'''

T = int(input())

for i in range(T):
    d = [1, 1, 1]
    N = int(input())
    for j in range(3, N):
        d.append(d[j-2]+d[j-3])
    print(d[N-1])
