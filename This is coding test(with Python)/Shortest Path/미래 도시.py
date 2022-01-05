import sys
input = sys.stdin.readline

INF = int(1e9)
# n: 회사의 개수, m: 경로의 개수
n, m = map(int, input().split())

# 그래프 생성
graph = [[INF for _ in range(n + 1)] for _ in range(n + 1)]
# 자기 자신에서 자기 자신으로 가는 비용
for node in range(1, n + 1):
    graph[node][node] = 0
# 간선 입력
for _ in range(m):
    node1, node2 = map(int, input().split())
    graph[node1][node2] = 1
    graph[node2][node1] = 1

# x: 판매할 회사, k: 소개팅 회사
x, k = map(int, input().split())

# Floyd_Warshall 알고리즘 사용
for now in range(1, n + 1):
    for node1 in range(1, n + 1):
        for node2 in range(1, n + 1):
            graph[node1][node2] = min(graph[node1][node2], graph[node1][now] + graph[now][node2])

#결과 출력
print(graph[1][k] + graph[k][x] if graph[1][k] + graph[k][x] < INF else -1)