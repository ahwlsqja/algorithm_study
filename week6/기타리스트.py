N, S, M = map(int, input().split())

V = list(map(int,(input()).split()))
'''
#dp 테이블에 각 곡의 볼륨 최대값을 저장한다.
#문제에서 결론적응로 최종적으로 가장 큰 볼륨이면 된다. 
#각 경우마다 볼륨을 줄이거나, 높이거나. 마지막 최종 볼륨이 중요한거지 각 단계별 볼륨 최대값은 중요하지 않다.
dp = [[] for _ in range(N+1)]
dp[0] = [S,S]

for i in range(len(V)):
    if len(dp[i]) == 0:
        print(-1)
        exit(0)
    for j in dp[i]:
        up = j + V[i]
        down = j - V[i]
        if up<0 or up>M:
            pass
        else:
            dp[i+1].append(up)

        if down<0 or down>M:
            pass
        else:
            dp[i+1].append(down)
        
print(max(dp[-1]))


# 위 코드의 문제점 앞의 모든 경우의 수를 배열로 다 갖고 있다. 메모리 사용량이 커진다. 
# 실제로는 각 단계의 가능한 볼륨 값들만 알면 되기 때문에 집합(set)이나 불리언 배열을 쓰면 메모리를 크게 줄일 수 있다. 
'''

#배열로 해도 메모리 초과가 난다. 
#집합으로 하면 해결!
dp= {S}

for i in range(len(V)):
    new_dp=set() # 빈 집합은 항상 이렇레 선언
    for j in dp:
        up = j + V[i]
        down = j - V[i]
        if 0<=up<=M:
            new_dp.add(up)
        if 0<=down<=M:
            new_dp.add(down)
    dp = new_dp
    if len(dp) == 0:
        print(-1)
        exit(0)
print(max(dp))
