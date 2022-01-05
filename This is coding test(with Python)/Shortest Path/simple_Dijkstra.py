#시간 복잡도: O(V^2), V = 간선의 개수

from _typeshed import StrPath
import sys
from typing import Tuple
input = sys.stdin.readline
INF = float('inf')

# 노드의 개수, 간선의 개수 입력 
n, m = map(int, input().split())
# 시작 노드 번호 입력
start = int(input())
# 그래프 리스트
graph = [[] for _ in range(n + 1)]
# 방문 체크 리스트
visited = [False] * (n + 1)
# 최단 거리 테이블 무한으로 초기화
distance = [INF] * (n + 1)

# 간선 입력
for _ in range(m):
    start_node, end_node, cost = map(int, input().split())
    graph[start_node].append[(end_node, cost)]

# 방문하지 않은 노드 중에서 최단 거리가 가장 짧은 노드 반환
def get_smallest_node():
    min_value = INF
    index = 0
    for i in range(1, n + 1):
        if distance[i] < min_value and not visited[i]:
            index = i
    return index

def dijkstra(start):
    distance[start] = 0
    visited[start] = True
    for j in graph[start]:
        distance[j[0]] = j[1]

    for i in range(n - 1):
        now = get_smallest_node()
        visited[now] = True

        for j in graph[now]:
            cost = distance[now] + j[1]
            if cost < distance[j[0]]:
                distance[j[0]] = cost
        
dijkstra(start)

for i in range(1, n + 1):
    # 도달할 수 없는 경우, 무한 출력
    if distance[i] == INF:
        print("INFINITY")
    # 도달할 수 있는 경우, 거리 출력
    else:
        print(distance[i])
    
