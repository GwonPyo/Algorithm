# 시간 복잡도 O(ElogV), V = 노드의 개수, E = 간선의 개수
import heapq
import sys
from types import GeneratorType
input = sys.stdin.readline
INF = float('inf')

# 노드의 개수, 간선의 개수 입력
n, m = map(int, input().split())
# 시작 노드 번호 입력
start = int(input())
# 그래프 리스트
graph = [[] for _ in range(n + 1)]
# 최단 거리 테이블
distance = [INF for _ in range(n + 1)]

for _ in range(m):
    start_node, end_node, cost = map(int, input().split())
    graph[start_node].append((end_node, cost))

def dijkstra(start):
    heap = []
    heapq.heappush(heap, (0, start))
    distance[start] = 0

    while heap:
        #최단 거리가 짧은 노드 꺼내기
        dist, now = heapq.heappop(heap)
        # 현재 노드가 처리된 적 있는 노드라면 무시
        if distance[now] < dist:
            continue
        # 현재 노드와 연결된 다른 인접한 노드 확인
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(heap, (cost, i[0]))

dijkstra(start)

for i in range(1, (n + 1)):
    if distance[i] == INF:
        print("INFINITY")
    else:
        print(distance[i])