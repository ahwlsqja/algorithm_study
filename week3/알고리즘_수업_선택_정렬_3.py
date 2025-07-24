class SegmentTree:
    def __init__(self, arr):
        self.n = len(arr)
        self.tree = [0] * (4 * self.n)
        self.arr = arr[:]
        self.build(1, 0, self.n - 1)
    
    def build(self, node, start, end):
        if start == end:
            self.tree[node] = start
        else:
            mid = (start + end) // 2
            self.build(2 * node, start, mid)
            self.build(2 * node + 1, mid + 1, end)
            
            left_idx = self.tree[2 * node]
            right_idx = self.tree[2 * node + 1]
            
            if self.arr[left_idx] >= self.arr[right_idx]:
                self.tree[node] = left_idx
            else:
                self.tree[node] = right_idx
    
    def query(self, node, start, end, l, r):
        if r < start or end < l:
            return -1
        
        if l <= start and end <= r:
            return self.tree[node]
        
        mid = (start + end) // 2
        left_idx = self.query(2 * node, start, mid, l, r)
        right_idx = self.query(2 * node + 1, mid + 1, end, l, r)
        
        if left_idx == -1:
            return right_idx
        if right_idx == -1:
            return left_idx
        
        if self.arr[left_idx] >= self.arr[right_idx]:
            return left_idx
        else:
            return right_idx
    
    def update(self, node, start, end, idx, val):
        if start == end:
            self.arr[idx] = val
        else:
            mid = (start + end) // 2
            if idx <= mid:
                self.update(2 * node, start, mid, idx, val)
            else:
                self.update(2 * node + 1, mid + 1, end, idx, val)
            
            left_idx = self.tree[2 * node]
            right_idx = self.tree[2 * node + 1]
            
            if self.arr[left_idx] >= self.arr[right_idx]:
                self.tree[node] = left_idx
            else:
                self.tree[node] = right_idx

n, k = map(int, input().split())
A = list(map(int, input().split()))

seg_tree = SegmentTree(A)
cnt = 0

for last in range(n-1, 0, -1):
    max_idx = seg_tree.query(1, 0, n-1, 0, last)
    
    if last != max_idx:
        cnt += 1
        if cnt == k:
            print(min(A[last], A[max_idx]), max(A[last], A[max_idx]))
            exit()
        
        # 교환
        A[last], A[max_idx] = A[max_idx], A[last]
        
        # 세그먼트 트리 업데이트
        seg_tree.update(1, 0, n-1, last, A[last])
        seg_tree.update(1, 0, n-1, max_idx, A[max_idx])

print(-1)