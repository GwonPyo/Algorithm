# My Solution(104ms)
'''
dfs와 bfs탐색 순서를 출력하면 되므로
각 방법으로 노드를 탐색함과 동시에 방문하는 노드를 순서대로 출력했다.
단, 문제에서 요구하는 데로 출력하려면 graph값을 sort해 줘야한다.
'''
import sys
from collections import deque
input = sys.stdin.readline

n, m, start = map(int, input().split())         # 노드의 개수, 간선의 개수, 시작 노드를 입력받는다.
graph = [[] for _ in range(n+1)]                # 양방향 그래프를 입력받을 리스트다.

for _ in range(m):                              # 간선을 입력받는다.
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1, n+1):                         # graph의 모든 원소를 정렬해준다.
    graph[i].sort()

visited = [False for _ in range(n+1)]           # dfs() 함수의 방문 여부를 체크해줄 리스트다.

def dfs(now):
    print(now, end=' ')                         # 현재 탐색하고 있는 노드를 출력하고 방문처리한다.
    visited[now] = True                         

    for i in graph[now]:                        # 연결된 모든 노드를 탐색한다.
        if not visited[i]:                      # 해당 노드를 방문하지 않았다면 해당 노드에 대해 dfs를 수행한다.
            dfs(i)

def bfs(start):
    visited = [False for _ in range(n+1)]       # bfs() 함수의 방문 여부를 체크해줄 리스트다.
    q = deque([start])                          # 큐를 생성하고 처음 시작점을 넣어준다.
    visited[start] = True                       # 시작점은 미리 방문처리 해놓는다.

    while q:
        now = q.popleft()                       # 큐에서 원소를 하나 꺼낸다.
        print(now, end = ' ')                   # 꺼낸 원소는 출력해준다.

        for i in graph[now]:                    # 연결된 모든 노드를 탐색한다.
            if not visited[i]:                  # 해당 노드를 방문하지 않았다면
                q.append(i)                     # 큐에 추가하고 방문처리해준다.
                visited[i] = True

dfs(start)
print()
bfs(start)
