'''
P_n은 I가 (n+1)개, O가 n개
''' 
#50점 답

N = int(input())
M = int(input())
S = input()

#I에 "OI"를 몇 번 더했느냐
p_n = "I" 
p_n = p_n + ("OI")*N


count = 0

for i in range(len(S)-len(p_n)+1): #범위 실수
    if S[i:i+len(p_n)] == p_n:
        count += 1
        
print(count)

''' 100점
import sys

N = int(sys.stdin.readline().strip())
M = int(sys.stdin.readline().strip())
S = sys.stdin.readline().strip()

P = 'IOI'

cnt = i = answer = 0

# 입력받은 S의 길이만큼 반복
while i < (M - 1):
  # 현재 반복되는 문자열이 'IOI'냐 ?
  if S[i : i+3] == P:
    # 그렇다면 다음에도 반복하는지 확인하기 위해 i+2
    i += 2
    # 'IOI' 반복 수 저장
    cnt += 1
    # 반복 수 cnt가 우리가 원하는 N과 동일하냐 ?
    if cnt == N:
      # 그렇다면 Pn을 찾은 것이므로 answer + 1
      answer += 1
      # 지금 Pn의 일부를 포함해서 또다른 Pn이 나올 수 있으므로 
      # cnt를 초기화하지 않고 -1만 함
      cnt -= 1

  # 현재 반복되는 문자열이 'IOI'가 아니냐 ?
  else:
    # 그럼 다음 인덱스로 이동
    i += 1
    # cnt 초기화
    cnt = 0

print(answer)
'''
