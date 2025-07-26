n, m = map(int, input().split())

if n==1 :
    ans = 1
elif n==2 :
    ans = min(4, (m-1)//2 + 1)
elif m < 7 :
    ans =  min(4, m)
else :
    ans = m - 2

print(ans)
