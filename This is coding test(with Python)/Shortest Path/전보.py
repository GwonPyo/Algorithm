import sys
import heapq
input = sys.stdin.readline

INF = int(1e9)
# n: 도시의 개수, m: 통로의 개수, c: 도시 C
n, m, c = map(int, input().split())

graph = [[]  for _ in range(n + 1)]
# 간선 입력
for _ in range(m):
    # x: 시작 도시, y: 도착 도시, z: 걸리는 시간
    x, y, z = map(int, input().split())
    graph[x].append((z, y))

# c에서 각 도시에 걸리는 시간을 기록할 리스트(distance)
distance = [INF] * (n + 1)

def dijkstra(start):
    heap = []
    distance[start] = 0
    heapq.heappush(heap, (0, start))

    while heap:
        # 최단 거리가 가장 짧은 노드 pop
        dist, now = heapq.heappop(heap)
        # 이미 처리된 노드의 경우 continue
        if distance[now] < dist:
                continue
        
        for i in graph[now]:
            cost = distance[now] + i[0]
            if cost < distance[i[1]]:
                distance[i[1]] = cost
                heapq.heappush(heap, (cost, i[1]))

dijkstra(c)

max_value = 0; count = 0
for i in range(1, n + 1):
    if distance[i] != INF:
        count += 1
        max_value = max(max_value, distance[i], max_value)

print(count - 1, max_value)