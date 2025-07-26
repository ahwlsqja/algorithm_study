student = []
for i in range(28):
    student.append(int(input()))

num = 1
answer = []
for i in range(1, 31):
    if i not in student:
        answer.append(i)

print(min(answer))
print(max(answer))


