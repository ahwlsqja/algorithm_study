count = 0
while(True):
    answer = 0
    L, P, V = map(int, input().split())
    if L == 0 and P == 0 and V == 0:
        break
    count += 1
    a = V % P
    flag = False
    while(True):
        if a <= L and flag == False:
            answer = ((V // P) * L + a)
            break
        elif a <=L and flag == True:
            break
        else:  
            answer = ((V // P) * L + L)
            a = a - L
            flag = True
    print(f"Case {count}: {answer}")

 

