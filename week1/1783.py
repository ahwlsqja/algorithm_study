# 병든 나이트

# 세로 1일때 여행 불가
# 세로 2일때 가로에 따라 1, 2, 4 가능
# 세로 3이상 일때 가로가 7보다 작으면 최대 4, 7보다 크면 모든 이동을 사용해서 가로-2칸 방문 가능
N, M = map(int, input().split())

if N == 1: print(1)
elif N ==2: print(min(4, (M-1)//2+1))
elif M < 7: print(min(4, M))
else: print(M-2)