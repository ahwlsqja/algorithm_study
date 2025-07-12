def solve():
    n = input().strip()
    
    # 각 숫자의 개수를 세기
    digits = [0] * 10
    digit_sum = 0
    
    for char in n:
        digit = int(char)
        digits[digit] += 1
        digit_sum += digit
    
    # 30의 배수 조건 확인
    # 1. 0이 최소 하나는 있어야 함 (10의 배수)
    if digits[0] == 0:
        print(-1)
        return
    
    # 2. 모든 자릿수의 합이 3의 배수여야 함
    if digit_sum % 3 != 0:
        print(-1)
        return
    
    # 가장 큰 수 만들기
    # 9부터 1까지 내림차순으로 배치하고, 마지막에 0들을 배치
    result = []
    
    # 9부터 1까지 배치
    for digit in range(9, 0, -1):
        result.extend([str(digit)] * digits[digit])
    
    # 0들을 마지막에 배치
    result.extend(['0'] * digits[0])
    
    # 결과 출력
    print(''.join(result))

solve()