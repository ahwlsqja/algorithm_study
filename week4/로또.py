def dfs(visit_ls,visited):
    if len(visit_ls) == 6:
        for i in range(6):
            print(visit_ls[i], end = " ")
        print()
        return #함수 끝내기
    
    for i in range(len(visited)):
        if visited[i] == False: #방문을 안했다면
            if visit_ls and S[i] <visit_ls[-1]: #오름차순으로만 방문해야함.
                continue
            visited[i] = True #방문처리
            dfs(visit_ls + [S[i]], visited) #visit_ls의 복사본을 사용하기
            visited[i] = False  # 다시 복구 (백트래킹)

while(True):
    ls = list(map(int, input().split()))
    if ls[0] == 0:
        break
    else:
        k = ls[0]
        S = ls[1:] #[1, 2, 3, 4, 5, 6, 7]
    #그래프 만들기
    '''
    graph = [[] for _ in range(50)]
    for i in range(len(S)):
        for j in range(i+1, len(S)):
            graph[S[i]].append(S[j])
    #print(graph)
    '''
    visited = [False]*len(S)
    dfs([], visited)
    print()



        

 

