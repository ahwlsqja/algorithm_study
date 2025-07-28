
import sys
X, Y = map(int, input().split())
Z = (Y*100//X) # Z = (Y//X) *100으로 작성하면 틀린다!!!!!!!!!!
#(Y//X)*100를 할때 X가 Y보다 무조건 같거나 크기 때문에 (Y//X) = 0이 나와서 그러지 않을까 싶습니다. -> 라는 블로그 댓글을 봤음 

if Z >= 99:
    print(-1)
    exit(0)
#print(Z)
def is_changed(a):
    temp_z = ((Y+a) *100 // (X+a))
    #print("temp+z", temp_z)
    return temp_z > Z
        
left = 1
right = sys.maxsize #상한값을 뭐로 해야할지 잘 모르겠음
answer = 0
while(left<=right):        
    mid = (left+right) // 2
    #print("mid", mid)
    if is_changed(mid):
        answer = mid #정답 갱신
        #print("answer", answer)
        right = mid - 1 #더 작은 값으로 탐색
        #print("right", right)
    else:
        left = mid + 1
        #print("left", left)

if answer == 0:
    print(-1)
else:
    print(answer)
        