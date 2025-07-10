# 모두의 마블
n = int(input())
cards = list(map(int, input().rstrip().split()))
cards.sort(reverse=True)

res = 0
first = cards[0]
for i in cards[1:]:
    val = first + i
    res += val

print(res)