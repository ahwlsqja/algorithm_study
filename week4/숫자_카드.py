N = int(input())
cards = list(map(int, input().split()))

M = int(input())
check = list(map(int, input().split()))

cards.sort()
answer = []
for i in check:
    find = False
    left = 0
    right = len(cards)-1
    target = i
    while(left<=right):
        mid = (left+right)//2
        #print("mid", mid)
        if cards[mid] == target:
            find = True
            answer.append(1)
            #print("answer", answer)
            break
        elif cards[mid] < target:
            left = mid + 1
            #print("left", left)
        else:
            right = mid - 1
            #print("right", right)
    if find == False:
        answer.append(0)
for j in answer:
    print(j, end=" ")




