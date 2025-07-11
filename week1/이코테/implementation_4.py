S = input()
num_sum = 0
s = []
for i in range(len(S)):
    if S[i].isdigit():
        num_sum += int(S[i])
    else:
        s.append(S[i])

s.sort()
a = ""
for i in s:
    a+=i
print(a, end="")
if num_sum!=0:
    print(num_sum)
