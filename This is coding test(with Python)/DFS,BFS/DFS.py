import sys
input = sys.stdin.readline


def dfs(graph, visited, start):
    visited[start] = True
    print(start, end = ' ')

    for next in graph[start]:
        if not visited[next]:
            dfs(graph, visited, next)
    
number_of_node = int(input())
number_of_edge = int(input())
graph = [[] for _ in range(number_of_node + 1)]

for _ in range(number_of_edge):
    node1, node2 = map(int, input().split())
    graph[node1].append(node2)
    graph[node2].append(node1)

visited = [False] * (number_of_node + 1)

dfs(graph, visited, 1)