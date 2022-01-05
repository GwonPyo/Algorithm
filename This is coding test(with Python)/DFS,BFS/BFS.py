from collections import deque
import sys

input = sys.stdin.readline

def bfs(graph, visited, start):
    queue = deque()
    queue.append(start)
    visited[start] = True

    while queue:
        now_location = queue.popleft()
        print(now_location, end = ' ')

        for next in graph[now_location]:
            if not visited[next]:
                visited[next] = True
                queue.append(next)
    

number_of_node = int(input())
number_of_edge = int(input())
graph = [[] for _ in range(number_of_node + 1)]

for _ in range(number_of_edge):
    node1, node2 = map(int, input().split())
    graph[node1].append(node2)
    graph[node2].append(node1)

visited = [False] * (number_of_node + 1)

bfs(graph, visited, 1)