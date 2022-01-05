# My Solution(112ms)
'''
0, 0에서 n-1, m-1로 가는 최단 거리를 구하면 되는 문제다.
따라서 bfs를 사용해 n-1, m-1에 도달하면 이동한 횟수를 반환했다.
'''
import sys
from collections import deque

n, m = map(int, input().split())                                    # 미로의 행과 열의 크기를 입력받는다.
graph = [list(map(int, list(input().rstrip()))) for _ in range(n)]  # 미로를 입력받는다.

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(x, y):
    q = deque([(x, y)])                                             # 큐에 시작점을 입력받는다.
    
    while q:
        x, y = q.popleft()                                          # 큐의 원소를 꺼낸다.                    

        if x == n-1 and y == m-1:                                   # 목표 지점에 도달했다면 해당 좌표의 원소를 반환하고 함수를 종료한다.
            return graph[x][y]                                      # 문제에서 무조건 이동 가능한 입력만 주어진다고 했으므로 도달하지 못하는 경우는 생각하지 않아도 된다.

        for i in range(4):                                          # 이동 가능한 모든 경로를 확인한다.
            nx = x+dx[i]; ny = y+dy[i]                              # 다음에 이동할 x, y 좌표다.

            if nx < 0 or nx >= n or ny < 0 or ny >= m:              # 인덱스 범위를 만족하지 않으면 반복문으로 돌아간다.
                continue
            '''
            아래와 같은 방식은 0, 0에서의 탐색을 최소 1, 최대 2번 더 수행한다.
            왜냐하면 graph[0][0]은 처음 탐색이후 1이란 값을 그대로 가지고, graph[nx][ny] == 1일때 q에 해당 좌표를 추가하기 때문이다.
            이를 방지하려면 방문여부를 확인하기 위한 visited 리스트를 만들어야 하는데
            이러한 방식보다 그냥 1~2회 더 탐색하는 것이 더 쉽고 코드가 간결하다 생각했다.(메모리도 늘어나고 조건문에 not visited[nx][ny]를 추가해야한다.)
            * 아니면 위에서 q에 (x, y)를 추가할 때, graph[x][y] = 2로 하고 n-1, m-1에 도달했을 때 출력을 graph[x][y]-1로 해주면 되긴 한다.
            그래도 동일하게 112ms를 소비한다.
            '''
            if graph[nx][ny] == 1:                                  # 해당 좌표가 길이라면(벽이 아니라면)
                q.append((nx, ny))                                  # 큐에다 저장해주고, 이전 graph값에 1을 더한 값을 저장한다.
                graph[nx][ny] = graph[x][y]+1

print(bfs(0, 0))