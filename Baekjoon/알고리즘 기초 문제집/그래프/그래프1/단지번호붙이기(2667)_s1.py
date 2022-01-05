# My Solution(68ms)
'''
아파트 단지의 개수와, 각 단지의 집 수를 오름차순으로 출력해야한다.
따라서 dfs를 수행해 몇 채의 집이 있는지 확인해 리스트에 저장하고 모든 탐색이 끝난 이후 정렬해줘야 한다.
이때, 리스트의 길이가 총 단지의 개수이다.
'''
import sys
input = sys.stdin.readline

n = int(input())                                                    # 지도의 한 변의 길이를 입력받는다.(지도는 정사각형이다.)
graph = [list(map(int, list(input().rstrip()))) for _ in range(n)]  # 지도의 정보를 입력받는다.

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

def dfs(x, y):
    global count                                                    # count를 이용해 몇 회의 dfs를 수행하는지 체크한다. (총 dfs의 횟수가 집의 개수가 된다.) 
    count += 1                                                      # count를 갱신한다.
    graph[x][y] = -1                                                # x, y좌표는 탐색을 한 것이므로 탐색처리를 위해 -1로 지정한다.(1이 아닌 다른 값이면 상관없다.)

    for i in range(4):                                              # 이동할 수 있는 모든 방향을 탐색해본다.
        nx = x+dx[i]; ny = y+dy[i]                                  # 다음에 이동할 x, y 좌표이다.
        if nx < 0 or nx >= n or ny < 0 or ny >= n:                  # 좌표가 인덱스 범위를 만족하지 않으면 반복문으로 돌아간다.
            continue

        if graph[nx][ny] == 1:                                      # 다음 좌표가 집이라면 해당 좌표에 대해 dfs를 수행해준다.
            dfs(nx, ny)

result = []                                                         # 각 단지의 집 개수를 저장할 리스트다.
count = 0                                                           # 단지를 탐색할 때 집의 개수를 체크해줄 변수다.
for x in range(n):                                                  # 모든 행과 열을 탐색한다.
    for y in range(n):
        if graph[x][y] == 1:                                        # 단지가 시작되는 지점이면
            dfs(x, y)                                               # dfs를 수행해 count를 갱신한다.
            result.append(count)                                    # 갱신된 count를 result에 저장하고 0으로 초기화한다.
            count = 0

result.sort()                                                       # 집의 개수를 오름차순으로 출력해야하므로 정렬한다.
print(len(result))                                                  # 총 단지의 개수와 각 단지의 집 개수를 출력한다.
print('\n'.join(map(str, result)))