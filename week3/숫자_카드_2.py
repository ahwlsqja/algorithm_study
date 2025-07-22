N = int(input())
nums = list(map(int, input().split()))
M = int(input())
find = list(map(int, input().split()))

dict = {} 
for i in nums:
    if i not in dict:
        dict[i] = 1
    else:
        dict[i] += 1

for i in find:
    if i in dict:
        print(dict[i], end =" ")
    else:
        print(0, end = " ")
