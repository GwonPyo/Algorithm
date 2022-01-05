from collections import deque
import sys
input = sys.stdin.readline

# n * m 크기의 배열로 표현되는 미로를 만들어야한다.
n, m = map(int, input().split())

# 미로를 담을 리스트 생성
maze = []

# 미로를 각 행마다 입력받는다. (총 n번 반복)
for _ in range(n):
    maze.append(list(map(int, list(input().rstrip()))))

# u, r, d, l 방향으로 이동시 변하는 인덱스 값을 담은 리스트들이다.
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

# 현재 위치에서 이동할 수 있는 좌표를 알려준다.
def able_to_move(index):
    result = []
    # u, r, d, l 총 4개의 방향으로 이동할 수 있다.
    # 따라서 4개의 방향중 이동할 수 있는 좌표를 result에 저장한다.
    for i in range(4):
        y = index[0] - dy[i]
        x = index[1] - dx[i]
        
        # maze의 범위를 벗어나는지 확인한다.
        if y < 0 or y >= n or x < 0 or x >= m:
            continue
        
        # 범위를 벗어나지 않는다면 이동할 수 있는 좌표인지 확인한다.
        # 이동 할 수 있는 좌표라면 이동 result 리스트에 추가한다.
        if maze[y][x] == 1:
            result.append((y, x))
    return result

# bfs 알고리즘을 이용해 탐색한다.
def bfs(start_y, start_x):
    # 시작점을 큐에 넣어준다.
    queue = deque([(start_y, start_x, 1)])
    # 시작점을 들렸으므로 더 이상 시작점으로 이동할 수 없도록
    # maze에서 시작점의 값을 0으로 바꾼다.
    maze[start_y][start_x] = 0

    while queue:
        y, x, result = queue.popleft()
        # 다음에 이동할 수 있는 좌표를 담은 able_next 리스트를 만든다.
        able_next = able_to_move((y, x))

        # 다음에 이동할 수 있는 좌표들이 목적지인지 확인한다.
        # 아니라면 bfs를 계속 수행한다.
        for y, x in able_next:
            if y == n - 1 and x == m - 1:
                print(result + 1)
            queue.append((y, x, result + 1))
            maze[y][x] = 0

bfs(0, 0)

# 1. 인덱스 확인 쉽게 하는법
# 위처럼 갈 수 있는 좌표인지 확인할 때 인덱스 범위를 확인하는 것이 귀찮다면
# 행과 열을 양 끝에 한 개씩 붙여 0으로 채워주면 되긴한다. (속도 증가 but 메모리도 증가)

# 2. 최단거리 출력 방식
# 위처럼 큐에 결과를 추가하고 이동한 곳의 값을 0으로 바꿔주는 것이 아니라
# maze리스트에 결과 값을 저장해도 문제가 없다. (메모리 절약가능)
# 단, (0, 0)로 몇 번더 이동할 수 있다. 하지만 결과에 문제는 없다.