import sys
input = sys.stdin.readline
INF = 1e10

n = int(input()) # 도시 개수
m = int(input()) # 버스 개수

graph = [[INF for _ in range(n+1)] for _ in range(n+1)] # cost를 저장할 graph를 선언한다.
for i in range(1, n+1): graph[i][i] = 0                 # i에서 i로 가는, 즉 동일한 지점으로 이동하는 값은 0으로 초기화한다.

for _ in range(m):
    start, end, cost = map(int, input().split())        # start에서 end로 이동할 때 필요한 cost를 입력받는다.
    graph[start][end] = min(graph[start][end], cost)    # graph[start][end]를 갱신한다.

for i in range(1, n+1):                                 # start에서 end로 갈 때 경유해야 하는 노드이다. 
    for start in range(1, n+1):
        for end in range(1, n+1):
            graph[start][end] = min(graph[start][end], graph[start][i] + graph[i][end])

for start in range(1, n + 1):                           # 올바르게 출력한다.
    for end in range(1, n + 1):
        if graph[start][end] == INF:
            print(0, end=' ')
        else:
            print(graph[start][end], end = ' ')
    print()
            
