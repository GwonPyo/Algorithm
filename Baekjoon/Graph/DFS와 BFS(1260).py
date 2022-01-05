from collections import deque
import sys
input = sys.stdin.readline
# n: 정점의 개수, m: 간선의 개수, v: 탐색을 시작할 번호
n, m, v = map(int, input().split())

# 간선을 입력 받을 그래프 생성
graph = [[] for _ in range(n + 1)]

# 간선 입력
for _ in range(m):
    node1, node2 = map(int, input().split())
    graph[node1].append(node2)
    graph[node2].append(node1)

# 번호가 낮은 순서부터 방문하기 위해 정렬해줌.
# Ex) 노드1에서 출발할때 연결된 곳이 8, 3, 4이면 3, 4, 8순으로 방문
for i in range(1, n + 1):
    graph[i].sort()

# dfs
def dfs(now, visited):
    # 현재 노드 방문 처리
    visited[now] = True
    print(now, end = ' ')

    for i in graph[now]:
        # 현재 노드와 이어진 노드가 방문하지 않았다면
        # 행당 노드로 이동
        if not visited[i]:
            dfs(i, visited)

def dfs2(start, visited):
    # dfs에 이용할 stack 생성
    stack = [start]
    visited[start] = True

    while stack:
        now = stack
# bfs
def bfs(start, visited):
    # 큐에 시작점을 추가해야 하므로 append를 사용하기 보단
    # 처음부터 리스트에 넣어주고 deque로 변환
    queue = deque([start])
    # 시작점 방문 처리
    visited[start] = True

    while queue:
        # 큐에서 값을 꺼냄
        now = queue.popleft()
        print(now, end = ' ')

        for i in graph[now]:
            # 현재 노드와 이어진 노드가 방문하지 않았다면
            # 해당 노드를 큐에 넣어주고 방문처리
            if not visited[i]:
                queue.append(i)
                visited[i] = True

# 방문 처리를 위한 visited 리스트 생성
visited = [False for _ in range(n + 1)]
dfs(v, visited)
print()
visited = [False for _ in range(n + 1)]
bfs(v, visited)