def lower_bound(arr, target):
    left, right = 0, len(arr)
    while left < right:
        mid = (left + right) // 2
        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid
    
    return left

def upper_bound(arr, target):
    left, right = 0, len(arr)
    while left < right:
        mid = (left + right) // 2
        if arr[mid] <= target:
            left = mid + 1
        else:
            right = mid
    
    return left

n = int(input())

cards = list(map(int, input().split()))

m = int(input())

queries = list(map(int, input().split()))

cards.sort()

result = []

for query in queries:
    left_idx = lower_bound(cards, query)
    right_idx = upper_bound(cards, query)
    count = right_idx - left_idx
    result.append(count)

print(' '.join(map(str, result)))