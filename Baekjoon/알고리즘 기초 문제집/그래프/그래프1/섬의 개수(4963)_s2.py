# My Solution(82ms)
'''
n*m개의 원소를 모두 탐색하면서 섬이 발견되면(1이라는 값을 가진 원소가 발견되면)
dfs를 실시해 해당 섬의 모든 값을 -1로 갱신한다. 또한 이렇게 dfs가 수행될 때 섬의 개수를 하나 씩 추가해준다.
'''
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

d_xy = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]   # 섬은 대각선, 양옆, 위아래 붙어 있으면 하나의 섬으로 센다.

while True:
    m, n = map(int, input().split())                                            # n: 지도의 행, m: 지도의 열
    if n == 0 and m == 0: break                                                 # n과 m의 입력이 0, 0으로 주어지면 반복문을 종료한다.

    graph = [list(map(int, input().split())) for _ in range(n)]                 # 지도를 입력받는다.

    def dfs(x, y):
        graph[x][y] = -1                                                        # 이미 확인한 섬들의 값은 -1로 지정한다.

        for dx, dy in d_xy:
            nx = x+dx; ny = y+dy                                                # 다음에 이동할 x, y 좌표다.
            if nx < 0 or nx >= n or ny < 0 or ny >= m:                          # 인덱스 범위를 만족하지 않으면 반복문으로 돌아간다.
                continue                            
            
            if graph[nx][ny] == 1:                                              # 다음 좌표가 섬이라면 해당 좌표에서도 dfs를 수행한다.
                dfs(nx, ny)

    result = 0
    for x in range(n):                                                          # 모든 행과 열을 탐색한다.
        for y in range(m):
            if graph[x][y] == 1:                                                # 어떠한 원소가 섬이라면(값이 1이라면)
                result += 1                                                     # 섬의 개수를 갱신하고 해당 좌표에서 dfs를 수행한다.
                dfs(x, y)

    print(result)                                                               # 결과를 출력한다.
