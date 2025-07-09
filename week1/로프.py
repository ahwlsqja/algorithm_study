N = int(input())
w = []
for i in range(N):
    n = int(input())
    w.append(n)

w.sort(reverse = True)

max_w = w[0] #최대로 들 수 있는 중량

for i in range(1, N):
    w_sum = w[i] * (i+1) #줄의 개수
    if max_w < w_sum:
        max_w = w_sum
    

print(max_w)

