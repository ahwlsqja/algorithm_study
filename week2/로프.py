N = int(input())
rope_list = [] 
for _ in range(N):
    rope_list.append(int(input()))

rope_list.sort(reverse=True)

max_weight = 0
for i in range(N):
    # i+1개의 로프 사용, 최솟값은 rope_list[i]
    current_weight = (i + 1) * rope_list[i]
    max_weight = max(max_weight, current_weight)

print(max_weight)