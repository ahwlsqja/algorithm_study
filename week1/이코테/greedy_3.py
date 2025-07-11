N = int(input())
ls = list(map(int, input().split()))

ls.sort()
#group = [0] * (N+1)
group = 0 #그룹 개수
count = 0 #인원 개수
for i in range(len(ls)):
    count += 1
    if i <= count:
        group += 1
        count = 0 #count = 0으로 하는 것을 생각못했음

print(group)
    