# My Solution(872ms)
'''
연결 요소의 개수란 그래프의 개수를 의미한다.
즉, 1-2-3-4-5 라는 그래프만 있다면 1개,
1-2-3, 4-5 총 2개의 그래프가 있다면 2를 출력하면 된다.
따라서 모든 원소를 dfs혹은 bfs로 탐색하고, 매번 탐색 수행시 그래프의 개수를 카운팅해주면 된다.
'''
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

n, m = map(int, input().split())        # n: 정점의 개수, m: 간선의 개수
graph = [[] for _ in range(n+1)]        # 양방향 그래프를 입력받는다.

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False for _ in range(n+1)]   # 방문 여부를 확인하기 위한 리스트다.

def dfs(now):       
    visited[now] = True                 

    for i in graph[now]:                # 현재 노드와 연결된 노드를 모두 탐색한다.
        if not visited[i]:              # 해당 노드를 방문한 적이 없다면 해당 노드에 대해 dfs를 수행한다.
            dfs(i)

result = 0                              # 그래프의 개수를 저장할 변수다.
for i in range(1, n+1):                 # 1~n까지 모든 노드를 탐색한다.
    if not visited[i]:                  # 해당 노드를 방문한 적이 없다면
        dfs(i)                          # 해당 노드에 대해 dfs를 수행하고 그래프 개수를 카운팅한다.
        result += 1

print(result)                           # 결과를 출력한다.
