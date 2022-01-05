import sys
from collections import deque
input = sys.stdin.readline

# 첫째 줄에는 컴퓨터의 수가 주어진다.
number_of_computer = int(input())  
# 둘째 줄에는 네트워크 상에 직접 연결된 컴퓨터 쌍의 수가 주어진다.
number_of_edge = int(input())
# 컴퓨터 번호에 맞게 접근하기 위해 컴퓨터 수보다 하나 더 이중 리스트를 생성한다.
graph = [[] for _ in range(number_of_computer + 1)]

# 양방향으로 그래프를 그린다.
for _ in range(number_of_edge):
    node1, node2 = map(int, input().split())
    graph[node1].append(node2)
    graph[node2].append(node1)

# 1번 컴퓨터랑 이어진 컴퓨터를 찾으면 된다.
# 따라서 dfs, bfs 어떤 방식을 써도 무방하다.
# 둘의 시간 복잡도는 동일하지만 일반적으로 bfs의 효율이 좋으므로 bfs 사용하자.
# 방문 여부를 확인할 리스트를 만든다.
visited = [False for _ in range(number_of_computer + 1)]
start = 1

def bfs():
    result = 0
    queue = deque()
    queue.append(start)
    visited[start] = True

    while queue:
        now = queue.popleft()
        for next in graph[now]:
            if not visited[next]:
                result += 1
                queue.append(next)
                visited[next] = True

    print(result)

bfs()