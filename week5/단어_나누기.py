s = list(map(str, input()))
#print(s)

answer = []
for i in range(1, len(s)-1):
    for j in range(i+1, len(s)):
        first = s[:i]
        #print(first)
        second = s[i:j]
        third = s[j:]

        first.reverse()
        second.reverse()
        third.reverse()

        answer.append("".join(first+second+third))

answer.sort()

print(answer[0])
