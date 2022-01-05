from collections import deque
from typing import MutableSequence
import sys

# n, m = map(int, input().split())

# graph = []
# for _ in range(n):
#     graph.append(list(map(int, list(input()))))

# queue = deque()
# queue.append((0, 0, 1))
# nn, nm = 0, 0
# dd = [(-1, 0), (1, 0), (0, -1), (0, 1)]

# while queue: 
#     nn, nm, count = queue.popleft()

#     if nn == n - 1 and nm == m - 1:
#         print(count)
#         break

#     for i in dd:
#         if nn + i[0] < 0 or nn + i[0] >= n or nm + i[1] < 0 or nm + i[1] >= m:
#             continue

#         if graph[nn + i[0]][nm + i[1]] == 1:
#             queue.append((nn + i[0], nm + i[1], count + 1))

n, m = map(int, input().split())

graph = []
for _ in range(n):
    graph.append(list(map(int, input())))

# 상하좌우 순서
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    queue = deque()
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue

            if graph[nx][ny] == 0:
                continue

            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))
    
    return graph[n - 1][m - 1]

print(bfs(0, 0))

# 2020.11.05 코드
input = sys.stdin.readline

n, m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, list(input().rstrip()))))

def bfs():
    movements = [(1, 0), (-1, 0), (0, -1), (0, 1)]
    queue = deque([(0, 0)])
    
    while queue:
        x, y = queue.popleft()
        for movement in movements:
            nx = x + movement[0] # 다음 행 인덱스
            ny = y + movement[1] # 다음 열 인덱스
            # 인덱스 범위를 넘지 않고, 해당 원소의 값이 1이라면 조건문을 실행한다.
            if (0 <= nx < n) and (0 <= ny < m) and graph[nx][ny] == 1:
                queue.append((nx, ny))
                graph[nx][ny] = graph[x][y] + 1
    
    return graph[-1][-1]
print(bfs())