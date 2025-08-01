N = int(input())
ls = list(map(int, input().split()))
sum_food = [0] * N

for i in range(len(ls)):
    if i == 0:
        sum_food[i] = ls[i]
        
    if i == 1:
        sum_food[i] = max(ls[i], ls[i-1])
    else:
        sum_food[i] = max(ls[i-1], ls[i-2]+ls[i])


print(sum_food[-1])
