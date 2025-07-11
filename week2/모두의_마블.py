n = int(input())
card_list = list(map(int, input().split()))
card_list.sort(reverse=True)
max_level = card_list[0]
max_gold = 0
for i in range(n-1):
    max_gold += (max_level+ card_list[i+1])

print(max_gold) 
