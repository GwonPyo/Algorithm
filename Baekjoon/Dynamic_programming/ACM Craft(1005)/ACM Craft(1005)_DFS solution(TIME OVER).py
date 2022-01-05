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
    graph = [[] for _ in range(n + 1)]
    # 출발점으로 가능한 노드의 번호를 얻기 위한 리스트

    for _ in range(k): # O(간선의 개수) => 최대 100,000
        start, end = map(int, input().split())
        graph[end].append(start)
        
    # aim = 목표 건축물
    aim = int(input())

    # 건물이 걸리는 시간을 저장할 리스트
    times = []
    stack = []
    time = 0
    stack.append((aim, 0))
    while stack: # O(간선의 개수) => 최대 100,000
        now, time = stack.pop() 
        time += construction_times[now]
        if not graph[now]:
            times.append(time)
            continue
        for i in graph[now]: # O(간선의 개수) => 최대 100,000
            stack.append((i, time))

    print(max(times))