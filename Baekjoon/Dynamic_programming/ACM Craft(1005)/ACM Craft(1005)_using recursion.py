import sys
input = sys.stdin.readline
# setrecursionlimit를 쓰지 않으면 resursion error 발생.
sys.setrecursionlimit(3000)
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

    def solution(now): 
        # dp가 -1이 아니라면 이전에 처리 되었거나
        # 출발점으로 가능한 건물이다.
        # 즉, 해당 건물의 최소 건축 시간은 이미 dp에 저장되어있다.
        if dp[now] != -1:
            return

        # 해당 건축 이전의 건물중 가장 오랜 시간이 걸리는 시간을 저장해야한다.
        pre_maxTime = float("-inf")
        for i in graph_array[now]:
            # 현재 건물 이전에 짓는 건물 중
            # dp에 저장된 값이 -1인 건물들은
            # 모두 solution함수를 이용해 채워준다.
            solution(i)
        for i in graph_array[now]:
            # 현재 건물 이전에 짓는 건물들의 최소 시간은 정해져있다.
            # 따라서 이전 시간중 가장 오래 걸린 시간을 선택해주면 된다.
            if pre_maxTime < dp[i]:
                pre_maxTime = dp[i]
        # dp를 설정한다.
        dp[now] = construction_times[now] + pre_maxTime

    solution(aim)
    print(dp[aim])
            