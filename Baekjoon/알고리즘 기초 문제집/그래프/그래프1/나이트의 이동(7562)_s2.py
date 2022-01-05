# My Solution(2172ms)
'''
나이트가 이동할 수 있는 모든 좌표로 이동하면서 해당 좌표에 도달할 때까지 bfs를 수행한다.
'''
import sys
from collections import deque
input = sys.stdin.readline

d_xy = [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1)] # 나이트가 이동할 수 있는 경로를 저장한 리스트다.

for _ in range(int(input())):                                                   # 테스트 케이스만큼 반복한다.
    n = int(input())                                                            # n: 체스판의 한 변의 길이
    start_x, start_y = map(int, input().split())                                # 나이트의 시작 좌표와 목표 좌표를 입력받는다.
    end_x, end_y = map(int, input().split())
    visited = [[False for _ in range(n)] for _ in range(n)]                     # 방문 여부를 체크하기 위한 리스트이다. 방문한 좌표에는 지금까지 방문한 좌표의 개수를 저장할 것 이다.

    def bfs(x, y):
        q = deque([(x, y)])                                                     # 큐를 생성하고 시작 좌표를 넣어준다.
        visited[x][y] = 1                                                       # 시작점의 visited 값을 1로 설정한다. (지금까지 방문한 좌표는 시작점 1개이기 때문이다.)

        while q:
            x, y = q.popleft()                                                  # 큐의 원소 하나를 꺼내준다.
            if x == end_x and y == end_y:                                       # 도착점에 도달했다면 지금까지 이동한 횟수를 반환하고 함수를 종료한다.
                return visited[x][y]-1
            
            for dx, dy in d_xy:                                                 # 이동가능한 방향으로 모두 이동해본다.
                nx = x+dx; ny = y+dy                                            # 이동하는 다음 x, y좌표이다.
                if nx < 0 or nx >= n or ny < 0 or ny >= n:                      # 좌표가 인덱스 번위를 만족하지 않는다면 반복문으로 돌아간다.
                    continue

                if not visited[nx][ny]:                                         # 해당 좌표를 방문한 적이 없다면
                    q.append((nx, ny))                                          # 큐에 추가하고, visited값을 갱신한다.
                    visited[nx][ny] = visited[x][y]+1

    print(bfs(start_x, start_y))