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
