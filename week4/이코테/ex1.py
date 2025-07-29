N, M = map(int, input().split())
length = list(map(int, input().split()))
left = 0
right = max(length)
flag = False
def calc_m(x): #x는 절단하는 높이
    sum_m = 0
    for l in length:
        if l < x:
            sum_m += 0
        else:
            sum_m += (l-x)
    return sum_m
mid = (left+right) // 2
while(left <= right):
    mid = (left+right) // 2
    if calc_m(mid) == M:
        print(mid)
        flag = True
        break
    elif calc_m(mid) > M:
        left = mid + 1   
    else:
        right = mid - 1

        
if flag == False:
    print(mid)   


