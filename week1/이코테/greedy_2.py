#<문제> 곱하기 혹은 더하기

s = input()
answer = 0

for i in range(len(s)):
    if answer == 0 or answer == 1:
        answer += int(s[i])
        continue
    if s[i] == '0' or s[i] == '1':
        answer += int(s[i])
    else:
        answer *= int(s[i])

print(answer)


'''
s = input()

answer = int(s[0])

for i in range(1, len(s)):
    num = int(s[i])
    if num <= 1 or answer <=1:
        answer += num
    else:
        answer *= num
print(answer)
'''

