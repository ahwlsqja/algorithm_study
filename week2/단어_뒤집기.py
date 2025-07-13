N = int(input())

for _ in range(N):
    my_list = [] 
    s = input()
    my_list = list(s.split(' '))
    result = []
    for reversing_s in my_list:
        result.append(reversing_s[::-1])
    print(' '.join(result))