# 완전 탐색 문제 
N = int(input())
time = ""
count = 0
for i in range(N+1):
    for j in range(60):
        for k in range(60):
            time = str(i) + str(j) + str(k)
            if '3' in time:
                count += 1
                time = ""

print(count)