N = int(input())

time = list(map(int, input().split()))
print(time)
time.sort()
print(time)
sum_time = 0
for i in range(N):
    for j in range(i+1):
        sum_time += time[j]

print(sum_time)