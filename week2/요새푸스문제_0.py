n, k = map(int, input().split())

# 1부터 n까지의 사람들을 리스트로 생성
people = list(range(1, n + 1))

# 제거된 사람들의 순서를 저장할 리스트
result = []

# 현재 위치를 나타내는 인덱스
current_index = 0

# 모든 사람이 제거될 때까지 반복
while people:
    # K번째 사람의 인덱스 계산 (0-based)
    current_index = (current_index + k - 1) % len(people)
    
    # 해당 사람을 제거하고 결과에 추가
    removed_person = people.pop(current_index)
    result.append(removed_person)
    
    # 리스트의 크기가 줄어들었으므로 인덱스 조정이 자동으로 됨
    # 단, current_index가 리스트 끝을 넘어서면 0으로 조정
    if current_index == len(people):
        current_index = 0

# 결과 출력
print('<' + ', '.join(map(str, result)) + '>')