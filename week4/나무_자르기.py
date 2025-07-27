def solve():
    n, m = map(int, input().split())
    trees = list(map(int, input().split()))

    left = 0
    right = max(trees)
    answer = 0
    while left <= right:
        mid = (left + right) // 2

        total_wood = 0

        for tree_height in trees:
            if tree_height > mid:
                total_wood += tree_height - mid
        
        if total_wood >= m:
            answer = mid
            left = mid + 1

        else:
            right = mid - 1
    print(answer)

solve()