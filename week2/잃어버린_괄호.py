s = input()
parts = s.split('-')

result = sum(map(int, parts[0].split('+')))
for i in range(1, len(parts)):
    result -= sum(map(int, parts[i].split('+')))

print(result)