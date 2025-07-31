## 목차
1. [순차 탐색](#1-linear_search)
2. [이진 탐색](#2-binary_search)

---

## 1. 이진 탐색

### 개념
- **이진 탐색**: 리스트 안에 있는 특정한 데이터를 찾기 위해 앞에서부터 데이터를 하나씩 확인하는 방법

### 시간 복잡도
- 단계마다 탐색 범위를 2로 나누는 것과 동일하므로 **연산 횟수**는 log2N에 비례함...(당연하다)
- 초기 데이터 개수가 32개 일때, 이상적으로 1단계를 거치면 16개 2단계를 거치면 8개 3단계를 거치면 4개 4단계를 거치면 2개... 
- 이렇게 이진 탐색을 탐색 범위를 절반씩!! 줄임
- O(logN)

### 구현 예제

**Python 코드**
```python
def binary_search(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2

    if array[mid] == target:
        return mid
    elif array[mid] > target:
        return binary_search(array, target, start, mid - 1)
    else:
        return binary_search(array, target, mid + 1, end)

n, target = list(map(int, input().split()))

array = list(map(int, input().split()))

result = binary_search(array, target, 0, n - 1)
if result == None:
    print("원소가 존재하지 않습니다!!")
else:
    print(result + 1)
```

파이썬에서선 이진탐색을 굉장히 쉽게 풀 수 있는 이진 탐색 라이브러리가 있다...
- bisect_left(a, x): 정렬된 순서를 유지하면서 배열 a에 x를 삽입할 가장 왼쪽 인덱스를 반환
- bisect_right(a, x): 정렬된 순서를 유지하면서 배열 a에 x를 삽입할 가장 오른쪽 인덱스를 반환

### 구현 예제

**Python 코드**
```python
from bisect import bisect_left, bisect_right

a = [1, 2, 4, 4, 8]
x = 4

print(bisect_left(a, x))
print(bisect_right(a, x))
```

**Python 코드**
```python
from bisect import bisect_left, bisect_right

def count_by_range(a, left_value, right_value):
    right_index = bisect_right(a, right_value)
    left_index = bisect_left(a, left_value)
    return right_index - left_index

# 배열 선언
a = [1, 2, 3, 3, 3, 3, 4, 4, 8, 9]

# 값이 4인 데이터 개수 출력
print(count_by_range(a, 4, 4))

# 값이 [-1, 3]범위에 있는 데이터 개수출력
print(count_by_range(a, -1, 3))
```

## 파라메트릭 서치(Parametric Search)
- 파라메트릭 서치란 최적화 문제를 결정 문제로 바꾸어 해결하는 기법임!
- 일반적으로 코딩 테스트에서 파라메트릭 서치 문제는 이진 탐색을 이용하여 해결할 수 있음!
---
### 문제 목록

#### 떡볶이 떡 만들기

**문제 설명**
- 떡볶이 떡의 길이가 일정하지 않은데 이걸 일정하게 맞추어 줘야함
- 절단기에 높이(H)를 지정해서 줄지어진 떡을 한 번에 절단해야함.. 높이가 H보다 긴 떡은 H 위의 부분이 잘릴 것이고, 낮은 떡은 잘리지 않음
- 예시로 높이가 19, 14, 10, 17 cm 인 떡이 가란히 있고 절단기 높이를 15cm로 지정하면 자른 뒤 떡의 높이는 15, 14, 10, 15 거 될 것임 그래서 잘린 떡의 길이는 차례대로 4, 0, 0, 2가 되어서 6cm만큼 가져가게 됨
- 적어도 M의 떡을 가져가기 위한 높이의 최댓값을 구하는 프로그램


**접근 방법**
- 적절한 높이를 찾을 때 까지 이진 탐색을 이용하여 높이 H를 반복하여 조정
- 조건의 만족 여부("예" 혹은 "아니요")에 따라서 탐색 범위를 좁혀서 해결
- 0부터 10억까지의 정수 중 하나를 정하면된다. 이렇게 엄청 큰 범위를 보면 이진 탐색을 떠올리면 됨..

**Python 코드(동빈나의 풀이)**
```python
n, m = list(map(int, input().split(' ')))
array = list(map(int, input().split()))

start = 0 
end = max(array)

result = 0
while(start <= end):
    total = 0
    mid = (start + end) // 2
    for x in array:
        if x > mid:
            total += x - mid
    
    if total < m:
        end = mid - 1
    
    else:
        result = mid 
        start = mid + 1

print(result)
```

---

#### 정렬된 배열에서 특정 수 개수 구하기

**문제 설명**
- x가 등장하는 횟수를 계산
- 수열 {1, 1, 2, 2, 2, 2, 3}이 있을 때 x = 2라면, 현재 수열에서 값이 2인 원소가 4개 이므로 4를 출력함
- 이 문제는 시간 복잡도 O(logN)이 아니면 시간 초과 판정을 받음

**접근 방법**
- 이진탐색

**Python 코드(동빈나의 풀이)**
```python
from bisect import bisect_left, bisect_right

def count_by_range(a, left_value, right_value):
    right_index = bisect_right(a, right_value)
    left_index = bisect_left(a, left_value)
    return right_index - left_index

# 배열 선언
a = [1, 2, 3, 3, 3, 3, 4, 4, 8, 9]

# 값이 4인 데이터 개수 출력
print(count_by_range(a, 4, 4))

# 값이 [-1, 3]범위에 있는 데이터 개수출력
print(count_by_range(a, -1, 3))
```

---

## 출처
- [이것이 취업을 위한 코딩 테스트다 with 파이썬](https://www.youtube.com/watch?v=2zjoKjt97vQ&list=PLRx0vPvlEmdAghTr5mXQxGpHjWqSz0dgC&index=2)

---












