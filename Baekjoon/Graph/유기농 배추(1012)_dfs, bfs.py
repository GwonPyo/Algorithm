import sys
from collections import deque
sys.setrecursionlimit(5000)
input = sys.stdin.readline

'''
보통 bfs로 푸는 것이 효율적이라고 알고 있어서 bfs로 풀었다.
하지만 정답자를 보니 bfs보다 dfs로 푼 사람이 많아 dfs로도 풀어보았다.
백준에서 RecursionError가 발생해 setrecursionlimit함수로 재귀 제한을 늘렸다.
+ 그냥 편한 방식을 풀면 될 것 같다.
'''

def dfs(row, col, arr):
    # row, col이 범위를 벗어나면 False를 반환하고 함수 종료
    if row < 0 or row >= len(arr) or col < 0 or col >= len(arr[0]):
        return False
    
    # 해당 위치의 값이 1이면 아래 코드 실행
    if arr[row][col] == 1:
        arr[row][col] = 0
        # 이동할 수 있는 곳으로 이동해 dfs실행
        # 범위에서 벗어나도 위에서 걸러지므로 상관이 없음.
        dfs(row + 1, col, arr)
        dfs(row - 1, col, arr)
        dfs(row, col - 1, arr)
        dfs(row, col + 1, arr)
        return True
    return False

for _ in range(int(input())):
    # 1 <= 가로 길이(m), 세로 길이(n) <= 50
    # 1 <= 배추 개수(k) <= 2500
    m, n, k = map(int, input().split())
    result = 0 # 결과를 저장할 변수
    arr = [[0 for _ in range(m)] for _ in range(n)] # 배추밭을 저장할 리스트(arr)

    # 배추 위치 입력
    for _ in range(k):
        col, row = map(int, input().split())
        arr[row][col] = 1
    
    # 탐색 시작
    for row in range(n):
        for col in range(m):
            if dfs(row, col, arr) == True:
                result += 1

    print(result)

'''
맨처음 bfs로 푼 방식이다.
원리는 위와 동일하다.
'''

def bfs(row, col, arr):
    movements = [(1, 0), (-1, 0), (0, -1), (0, 1)]
    queue = deque([(row, col)])
    arr[row][col] = 0

    while queue:
        row, col = queue.popleft()
        for move_r, move_c in movements:
            # 위치를 이동시킨다.
            next_row = row + move_r
            next_col = col + move_c
            # 이동한 위치가 배열의 범위를 넘었는지 확인한다.
            if next_row < 0 or next_row >= len(arr) or next_col < 0 or next_col >= len(arr[0]):
                continue
            # 범위를 넘지 않았다면 무가 있는지 확인한다.
            if arr[next_row][next_col] == 1:
                arr[next_row][next_col] = 0
                queue.append((next_row, next_col))

for _ in range(int(input())):
    # 1 <= 가로 길이(m), 세로 길이(n) <= 50
    # 1 <= 배추 개수(k) <= 2500
    m, n, k = map(int, input().split())
    result = 0
    arr = [[0 for _ in range(m)] for _ in range(n)]

    for _ in range(k):
        col, row = map(int, input().split())
        arr[row][col] = 1
        
    for row in range(n):
        for col in range(m):
            # 해당 위치에 무가 있으면 아래 코드 실행
            if arr[row][col] == 1:
                # bfs를 실행에 인접 무 위치의 값을 0으로 바꿔줌
                bfs(row, col, arr)
                result += 1

    print(result)