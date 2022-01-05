import sys
input = sys.stdin.readline
INF = float("inf")
# 테이스케이스 개수 입력
test_case = int(input())

for _ in range(test_case): # O(테스트 횟수)
    # n: 건물의 개수, k: 건물간의 건설 순서 규칙
    n, k = map(int, input().split())

    # construction_times: 구조물 건축 시간을 저장한 리스트
    construction_times = [0] + list(map(int, input().split()))

    # graph: 건물간의 간선을 저장하기위한 그래프 리스트
    graph_array = [[] for _ in range(n + 1)]
    # able_to_start: 출발점으로 가능한 건물들을 담아놓는 리스트.
    able_to_start = [True for _ in range(n + 1)]
    dp = [-1 for _ in range(n + 1)]

    for _ in range(k): # O(간선의 개수) => 최대 100,000
        start, end = map(int, input().split())
        graph_array[end].append(start)
        able_to_start[end] = False

    for i in range(1, n + 1): # O(건물의 개수) => 최대 1,000
        # 출발점으로 가능한 건물들은
        # 그 건물의 건설 시간이 최소 시간이다.
        # 따라서 dp에 해당 건물의 건축 시간을 입력한다.        
        if able_to_start[i]:
            dp[i] = construction_times[i]

    aim = int(input())
    stack = []

    if dp[aim] == -1:
        stack.append(aim)
    
    # setresursionlimit 대신 resursion error 해결책으로 
    # 스택을 사용해봤다.
    while stack:
        now = stack.pop()

        for i in graph_array[now]:
            if dp[i] == -1:
                stack.append(now)
                stack.append(i)
                continue
        
        pre_maxTime = float("-inf")
        for i in graph_array[now]:
            if pre_maxTime < dp[i]:
                pre_maxTime = dp[i]
        
        dp[now] = construction_times[now] + pre_maxTime
    
    print(dp[aim])
            