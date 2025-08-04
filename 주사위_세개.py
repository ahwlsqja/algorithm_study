ls = list(map(int, input().split()))
count = [0]*7
for i in range(len(ls)):
    count[ls[i]] += 1
max_num = 0
for i in range(len(count)):
    if count[i] == 3:
        print(10000 + i*1000)
        exit(0)
    if count[i] == 2:
        print(1000 + i * 100)
        exit(0)
    if count[i] == 1:
        max_num = max(max_num, i)

print(max_num*100)
