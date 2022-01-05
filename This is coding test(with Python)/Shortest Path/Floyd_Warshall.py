import sys
input = sys.stdin.readline

INF = float("inf")

n = int(input())
m = int(input())

graph = [[INF for _ in range(n + 1)] for _ in range(n + 1)]

# 자기 자신에서 자기 자신으로 가는 비용은 0으로 초기화
for i in range(1, n + 1):
    graph[i][i] = 0

# 간선의 정보 입력
for _ in range(m):
    start_node, end_node, cost = map(int, input().split())
    graph[start_node][end_node] = cost

# 플로이드 워셜 알고리즘 수행
for now in range(1, n + 1):
    for node1 in range(1, n + 1):
        for node2 in range(1, n + 1):
            graph[node1][node2] = min(graph[node1][node2], graph[node1][now] + graph[now][node2])

for node1 in range(1, n + 1):
    for node2 in range(1, n + 1):
        if graph[node1][node2] == INF:
            print("INFINITY", end = ' ')
        else:
            print(graph[node1][node2], end = ' ')
    print()
