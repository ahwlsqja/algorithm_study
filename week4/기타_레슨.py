'''
N, M = map(int, input().split())
lectures = list(map(int, input().split()))
lectures.sort()
#탐색: 블루레이의 크기
left = 1
right = sum(lectures)
#하나의 블루레이에 담기는 곡의 시간이 최대가 되어야 블루레이 하나의 크기가 최소가 될 수 있다.
#하나의 블루레이에 담기는 곡의 시간을 적절히 분배하지 않고 최소최소최대로 담으면 결국 가능한 블루레이 크기가 커지므로 이는 최소 블루레이 크기를 구할 수 없다. 
while(left<=right):
    mid = (left + right)//2
    sum_lec = 0 
    bluelay_size = []
    for i in range(N):
        if (i != N-1) and ((sum_lec + lectures[i+1]) > mid):
            bluelay_size.append(sum_lec)
            sum_lec = 0
        if (i == N-1):
            if (sum_lec + lectures[i])<=mid:
                bluelay_size.append(sum_lec)
        sum_lec += lectures[i]
    if len(bluelay_size) == M:
        print(mid)
        exit(0)
    elif len(bluelay_size) < M: #블루레이 개수가 적게나오면 한 블루레이에 담기는 강의시간을 줄여야한다.
        right = mid -1
    else: #블루레이 개수가 더 많게 나오면? 한 블루레이에 담기는 강의시간을 늘려야한다.
        left = mid + 1
'''
N, M = map(int, input().split())
lectures = list(map(int, input().split()))

#탐색: 블루레이의 크기
left = max(lectures)
right = sum(lectures)
#하나의 블루레이에 담기는 곡의 시간이 최대가 되어야 블루레이 하나의 크기가 최소가 될 수 있다.
#하나의 블루레이에 담기는 곡의 시간을 적절히 분배하지 않고 최소최소최대로 담으면 결국 가능한 블루레이 크기가 커지므로 이는 최소 블루레이 크기를 구할 수 없다. 
def is_valid(bluelay_size):
    #print("bluelay_size", bluelay_size)
    if len(bluelay_size) <= M:
        return True
    else:
        return False

answer = 0
mid = 0
while(left<=right):
    mid = (left + right)//2
    sum_lec = 0 
    bluelay_size = []
    for i in range(N):
        #print("mid", mid)
        #print("i", i)
        #print("sum_lec", sum_lec)
        #print("sum_lec + i", sum_lec + lectures[i])
        if sum_lec + lectures[i] > mid:
            bluelay_size.append(sum_lec)
            sum_lec = 0
        sum_lec += lectures[i]
    # 마지막 블루레이 한 번 더 담아줘야 해!
    bluelay_size.append(sum_lec)
    if is_valid(bluelay_size): #블루레이 개수가 적게나오면 한 블루레이에 담기는 강의시간을 줄여야한다.
        answer = mid #정답이 될 수 있는 mid저장
        right = mid -1
    else: #블루레이 개수가 더 많게 나오면? 한 블루레이에 담기는 강의시간을 늘려야한다.
        left = mid + 1
    

print(answer)

