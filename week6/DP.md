## 다이나믹 프로그래밍(DP)

### 1. 개념
- 메모리를 적절히 사용하여 수행 시간 효율성을 비약적으로 향상시키는 방법임.
- 동적 계획법 이라고도 부르며 프로그램이 실행되는 도중이 실행에 필요한 메모리를 할당하는 기법을 동적 할당이라고 함.
- 하지만 다이나믹 프로그래밍에서는 별다른 의미없이 쓰인 단어

다이나믹 프로그래밍은 문제가 다음의 조건을 만족할 때 사용할 수 있음.
1. 최적 부분 구조(Optimal Substructure)
2. 중복되는 부분 문제(Overlapping Subproblem)

#### 1.1 피보나치 수열 
이를테면 피보나치 수열은
<img width="816" height="131" alt="image" src="https://github.com/user-attachments/assets/5db249f4-8f19-4162-bfab-34aafa78ec46" />
과 같은 수열이다. 
**점화식**은 인접한 항들 사이의 관계식을 의미하며 피보나치 수열을 점화식으로 표현하면 다음과 같음.
<img width="1002" height="145" alt="image" src="https://github.com/user-attachments/assets/8c0483bf-d3ed-4c0a-871c-2868e18ee722" />
<img width="1525" height="496" alt="image" src="https://github.com/user-attachments/assets/3400fa9a-07f5-4af0-bd10-e270b12b5f4d" />
이런식으로 피보나치 수열이 계산되며 프로그래밍에서는 이러한 수열을 배열이나 리스트를 이용해 표현한다.
아래와 같이 이진 트리 형태로 구현이 가능하며 n번째 피보타치 수를 f(n)라고 할 때 4번째 피보나치 수 f(4)를 구하는 과정을 아래와 같다. 
<img width="590" height="552" alt="image" src="https://github.com/user-attachments/assets/3ccfabb6-b14a-4741-9c65-eadb214b4d4a" />

따라서 피보나치 수열을 Python 단순 재귀로 표현하면 
```python
def fibo(x):
  if x == 1 or x == 2:
    return 1
  return fibo(x - 1) + fibo(x - 2)

print(fibo(4))
```
이 나오고 실행결과는 3이다. 
#### 1.2 피보나치 수열의 시간 복잡도 
- 단순 재귀 함수로 피보나치 수열을 해결하면 지수 시간 복잡도를 가지게 된다.
- 다음과 같이 f(n)가 여러 번 호출되는 것을 확인할 수 있음.
<img width="1160" height="598" alt="image" src="https://github.com/user-attachments/assets/9a2a1c60-7f8d-48d7-bcee-c5d4a9c4b2d6" />
따라서 피보나치 수열의 시간 복잡도는
<img width="1485" height="437" alt="image" src="https://github.com/user-attachments/assets/827d4a54-e72c-43e1-805b-2144b1af4f6f" />
과 같고 연산량이 엄청 많이지게됨.

#### 1.3 다이나믹 프로그래밍의 사용 조건
다이나믹 프로그래밍의 사용 조건을 만족하는지 확인해야하는데 
사용 조건으로는
1. 최적 부분 구조: 큰 문제를 작은 문제로 나눌 수 있는지
2. 중복되는 부분 문제: 동일한 작은 문제를 반복적으로 해결하는지
이 두 가지 조건을 만족해야한다.

위에서 알아봤던 피보나치 수열은 이 다이나믹 프로그래밍의 조건을 만족한다고 볼 수 있음.

#### 1.4 메모이제이션 
- 메모이제이션은 다이나믹 프로그래밍을 구현하는 방법 중 하나임.
- 한 번 계산한 결과를 메모리 공간에 메모하는 기법임.
  - 같은 문제를 다시 호출하면 메모했던 결과를 그대로 가져오는 것
  - 값을 기록해 놓는다는 점에서 **캐싱(Caching)**이라고도 함

#### 1.5 탑다운 vs 보텀업
- 탑다운 방식은 **하향식**이라고도 하며 보텀업 방식은 **상향식**이라고도 함.
- 다이나믹 프로그래밍의 전형적인 형태는 보텀업 방식임.
  - 결과 저장용 리스트는 **DP 테이블**이라고 명명함
- 메모이제이션은 이전에 계산된 결과를 일시적으로 기록해 놓는 넓은 개념을 의미 한다고 생각하면 된다. 그래서 캐싱!!
- 안쓸 수도 있지만 일단 담아놓자!

탑다운
```python
d = [0] * 100

def fibo(x):
  if x == 1 or x == 2:
    return 1

  if d[x] != 0:
    return d[x]

  d[x] = fibo(x - 1) + fibo(x - 2)
  return d[x]

print(fibo(99))
```
일종의 트리라고 볼 수 있는데 메모이제이션 덕에 자식노드가 적은 트리를 완성할 수 있다.
<img width="785" height="435" alt="image" src="https://github.com/user-attachments/assets/2abd9a4d-1b46-4292-9acd-33cef46194cc" />


보텀업
```python
d = [0] * 100

d[1] = 1
d[2] = 1
n = 99

for i in range(3, n + 1):
  d[i] = d[i - 1] + d[i - 2]

print(d[n])
```

#### 1.6 다이나믹 프로그래밍 vs 분할 정복
다이나믹 프로그래밍과 분할 정복은 모두 **최적 분할 구조**를 가질 때 사용할 수 있음.
- 큰 문제를 작은 문제로 나눌 수 있으며 작은 문제의 답을 모아서 큰 문제를 해결 할 수 있는 상황
다이나믹 프로그래밍과 분할 정복의 차이점은 **부분 문제의 중복**이라고 할 수 있다.
- 다이나믹 프로그래밍 문제에서는 각 부분 문제들이 서로 영향을 미치며 부분 문제가 중복되지만
- 분할 정복 문제에서는 동일한 부분 문제가 반복적으로 계산되지 않음.


#### 1.7 다이나믹 프로그래밍 접근
- 주어진 문제가 **다이나믹 프로그래밍**유형임을 파악하는게 중요!
- 가장 먼저 그리디, 구현, 완전 탐색 등의 아이디어로 문제를 해결할 수 있는지 검토를 해야함
- 일단 재귀함수로 완전 탐색으로 짠 뒤에 작은 문제에서 구한 답이 큰 문제에서 그대로 사용될 수 있으면, 코드를 개선
- 일반적인 코딩 테스트 수준에서는 기본 유형의 다이나믹 프로그래밍 문제가 출제됨 -> 어려워 지면 한없이 어려워 지기 때문!

### 개미 전사 문재
<img width="1156" height="482" alt="image" src="https://github.com/user-attachments/assets/c2f83048-c6d5-43bd-8981-f10453428249" />
이런 문제입니다..
<img width="1175" height="457" alt="image" src="https://github.com/user-attachments/assets/889ed23d-2a95-403e-bb52-1e45c5a809eb" />
이런식입니다...
<img width="1091" height="392" alt="image" src="https://github.com/user-attachments/assets/bbfc3803-3009-414f-a2d1-2d04723fcfac" />
이렇게 점화식을 세울 수 있음. 

```python
n = int(input())
array = list(map(int, input().split()))
d = [0] * 100
d[0] = array[0]
d[1] = max(array[0], array[1])
for i in range(2, n):
  d[i] = max(d[i - 1], d[i - 2] + array[i])
print(d[n - 1])
```
처음에는 이 문제가 뭔 말인가... 하고 되게 헷갈려서 이해하는데 오래걸렸는데 사실 저 창고 개수 4개는 예시이고 전혀 관련이 없습니다. 그냥 안겹치게 최대의 개수를 구하면 되는 문제입니다.

### 1로 만들기
<img width="1157" height="436" alt="image" src="https://github.com/user-attachments/assets/b539b6d4-95f9-4d4c-9d12-380190773c47" />
이런 문제입니다...
<img width="1114" height="471" alt="image" src="https://github.com/user-attachments/assets/641875ad-a039-470e-b78c-9bc2b4726606" />
이 문제를 보고 오해하면 안되는건 그리디에서나온 1이 되는 문제하고 굉장히 다르다... 그리디는 1를 빼는거 보다 나누는게 값을 휠씬 많이 줄일 수 있기 때문에 매 상황마다 나누는 식으로 진행하였지만, 이 문제는 아니다!
예를 들면 26 -> 25 -> 5 -> 1 이런 경우가 그 경우에 해당!!
<img width="1146" height="476" alt="image" src="https://github.com/user-attachments/assets/70c119a8-2dac-48d6-956e-163c5801fd21" />

<img width="1079" height="439" alt="image" src="https://github.com/user-attachments/assets/c6d993a0-61bf-481f-8300-9bb305a23f9c" />

```python
x = int(input())
d = [0] * 30001
for i in range(2, x + 1):
  d[i] = d[i-1] + 1
  if i % 2 == 0:
    d[i] = min(d[i], d[i // 2] + 1)
  if i % 3 == 0:
    d[i] = min(d[i], d[i // 3] + 1)
  if i % 5 == 0:
    d[i] = min(d[i], d[i // 5] + 1)

print(d[x])
```
이런 식으로 코드를 짤 수 있수가 있다. 처음에 이 코드를 보고 굉장히 이해가 안되서 이해하는데 꽤 오래 걸렸다..
일단 d[i] = d[i-1] + 1 에서 왜 1을 더할까... 고민을 했는데 그냥 단순히 d[i]는 i값에서의 연산의 수 라고 보면 된다. 그래서 d[i] 이 d[i-1]에서 +1을 하면 되는거고 그게 사실상 연산이 하나 추가되는것 이므로 이렇게 적을 수 있는 것이다.

그리고 아래에서 나와있는 나누기에서 min을 해서 고르는거에서 나누는걸아 1을 뺸거랑 비교해서 고르게 되있는거다. 그래서 그 값에 대한 연산개수를 d[i]에 저장하고!! 일단 이런식으로 된
보텀업 방식으로 풀린다는게 좀 직관적으로 이해하기가 어려운거 같다..

### 화폐 만들기 
<img width="1135" height="351" alt="image" src="https://github.com/user-attachments/assets/6b8bbc05-8005-47ab-abae-64e19caba1d8" />
<img width="797" height="332" alt="image" src="https://github.com/user-attachments/assets/751f3ad7-6b42-4708-8a54-0645ec20b228" />
<img width="1130" height="451" alt="image" src="https://github.com/user-attachments/assets/7bb852ab-bdc7-4039-8ec6-e3703fb5f0a2" />
<img width="1124" height="482" alt="image" src="https://github.com/user-attachments/assets/2fd62cd3-fe3f-46dd-bf25-8e1ae63fe107" />
<img width="1118" height="462" alt="image" src="https://github.com/user-attachments/assets/04c04524-cc46-49a2-8add-2007052a0a00" />

```python
n, m = map(int, input().split())
array = []
for i in range(n):
  array.append(int(input())

d = [10001] * (m + 1)

d[0] = 0
# i는 화폐 단위, j는 금액을 의미한다.
for i in range(n):
  for j in range(array[i], m+1):
    if d[j - array[i]] != 10001:
      d[j] = min(d[j], d[j - array[i]] + 1)

if d[m] == 10001:
  print(-1)
else:
  print(d(m))
```

아... 내가 DP에 대해서 잘 모르는 것도 있지만 이 코드도 연신 1시간을 보고서야 이해가 되었다..
물론 클로드의 도움을 받았지만 
일단 초기상태를 

```
d[0]=0, d[1]=10001, d[2]=10001, ..., d[15]=10001
```


이런식으로 된다는 것을 문제를 분들이라면 알것이다. 근데 문제는 그 다음부터 좀 이해가 안됬는데

```python
for i in range(n):                    # 각 화폐에 대해
    for j in range(array[i], m + 1):  # 해당 화폐 이상의 모든 금액에 대해
        if d[j - array[i]] != 10001:  # 이전 금액이 만들어질 수 있다면
            d[j] = min(d[j], d[j - array[i]] + 1)
```

이 부분이다. 코드가 일단 굉장히 가독성이 떨어졌다 나에겐 그래서 클로드에게 도움을 요청했는데 
클로드는 구체적인 예시를 들어서 설명을 해줬다. 
일단 화폐[2, 3]원, 목표 15원을 설정하였는데
이런 예시를 코드에 집어넣으면

```python
for j in range(2, 16):  # j = 2, 3, 4, 5, ..., 15
    if d[j - 2] != 10001:  # (j-2)원이 만들어질 수 있다면
        d[j] = min(d[j], d[j - 2] + 1)
```
이런식이 되었다. 그래서 
j=2일 때:
- d[2-2] = d[0] = 0 (만들 수 있음!)
- d[2] = min(10001, 0 + 1) = 1
- 의미: 0원에 2원 화폐 1개 추가 → 2원 완성
이고 
j=4일 때:
- d[4-2] = d[2] = 1 (만들 수 있음!)
- d[4] = min(10001, 1 + 1) = 2
- 의미: 2원에 2원 화폐 1개 추가 → 4원 완성 (화폐 2개)
이다

그래서 다들 아시겠지만 최종답은 15가 나온다고 한다... 
조건문에 따르면 그 값이 끝끝내 안나오면 -1로 처리를 하고..

### 금광
<img width="1135" height="473" alt="image" src="https://github.com/user-attachments/assets/783055f4-fc84-4f6d-85c6-484114cfa5e7" />
<img width="1501" height="783" alt="image" src="https://github.com/user-attachments/assets/135f6ee1-378c-48cf-889f-53d56e31f828" />
<img width="1688" height="770" alt="image" src="https://github.com/user-attachments/assets/bde30145-5b13-48e9-9a74-8d54abd490b0" />
<img width="1757" height="687" alt="image" src="https://github.com/user-attachments/assets/2eb5e716-b25f-4cf3-8f1a-d4984f0d7f18" />
<img width="1721" height="789" alt="image" src="https://github.com/user-attachments/assets/a866a843-f0bf-45c6-92dc-cacdf61e1f80" />
클로드 형이 아주 이해하기 쉽게 알려주었따..
<img width="830" height="752" alt="image" src="https://github.com/user-attachments/assets/a60dbec6-266e-404d-8859-00e4230142ea" />

```python
for tc in range(int(input())):
    # 금광 정보 입력
    n, m = map(int, input().split())
    array = list(map(int, input().split()))

    # 다이나믹 프로그래밍을 위한 2차원 DP 테이블 초기화
    dp = []
    index = 0
    for i in range(n):
        dp.append(array[index:index + m])
        index += m

    # 다이나믹 프로그래밍 진행
    for j in range(1, m):
        for i in range(n):
            # 왼쪽 위
            if i == 0:
                left_up = 0
            else:
                left_up = dp[i - 1][j - 1]
            # 왼쪽 아래
            if i == n - 1:
                left_down = 0
            else:
                left_down = dp[i + 1][j - 1]
            # 왼쪽
            left = dp[i][j - 1]
            # 현재 위치에 이전 값 더해서 최댓값 저장
            dp[i][j] = dp[i][j] + max(left_up, left_down, left)

    result = 0
    for i in range(n):
        result = max(result, dp[i][m - 1])

    print(result) 
```
### 병사 배치하기 
<img width="1147" height="309" alt="image" src="https://github.com/user-attachments/assets/7f0c07b4-72f1-48a4-b7eb-00cbf685c20e" />
<img width="1132" height="474" alt="image" src="https://github.com/user-attachments/assets/df395d32-7ced-4010-9d1d-6cb6893b0cf5" />
<img width="1032" height="447" alt="image" src="https://github.com/user-attachments/assets/8630753c-116f-4306-a2d1-523928d01b17" />
<img width="1136" height="407" alt="image" src="https://github.com/user-attachments/assets/89791a19-5937-4642-a5d1-7a90949c2c5f" />
<img width="1104" height="323" alt="image" src="https://github.com/user-attachments/assets/78074cf7-c5c0-4b69-bd1f-bb0bb8aeed33" />
<img width="1152" height="506" alt="image" src="https://github.com/user-attachments/assets/97b7a25e-9e8e-4184-9ef1-7d6fcff0ff15" />

동빈나 형님은 LIS를 Reverse 시키서 불면된다고 한다..

```python
n = int(input())
array = list(map(int, input().split()))

# 순서를 뒤집어 '최장 증가 부분 수열' 문제로 변환
array.reverse()

# 다이나믹 프로그래밍을 위한 1차원 DP 테이블 초기화
dp = [1] * n

# 가장 긴 증가하는 부분 수열(LIS) 알고리즘 수행
for i in range(1, n):
    for j in range(0, i):
        if array[j] < array[i]:
            dp[i] = max(dp[i], dp[j] + 1)

# 열외해야 하는 병사의 최소 수 출력
print(n - max(dp))
```
