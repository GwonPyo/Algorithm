import sys
import heapq
input = sys.stdin.readline

INF = 10e9

n, m = map(int, input().split())
start = int(input())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    node1, node2, distance = map(int, input().split())
    graph[node1].append((distance, node2))

result = [INF for _ in range(n+1)]
q = []
heapq.heappush(q, (0, start))

while q:
    value, now = heapq.heappop(q)
    if result[now] <= value: continue
    else: result[now] = value
    
    for distance, i in graph[now]:
        heapq.heappush(q, (value+distance, i))

for i in result[1:]:
    print('INF') if i==INF else print(i)


