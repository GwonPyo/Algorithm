from collections import deque
import sys
input = sys.stdin.readline

# 정사각형 변의 길이(n)
n = int(input())

# 아파트 단지를 입력할 리스트(apartment)
# 방문할 때 위, 아래, 왼쪽, 오른쪽을 모두 확인해야한다.
# 그냥 배열을 확인하면 모서리 밑 변의 끝 부분을 예외로 두고 코딩해야한다.
# 하지만 위아래, 양 옆을 0으로 채우면 그럴 필요가 없다.
apartment = [[0 for _ in range(n + 2)]]
# 아파트 단지 입력
for _ in range(n):
    apartment.append([0] + list(map(int, list(input().rstrip()))) + [0])
# 아래를 0으로 채운다.
apartment.append([0 for _ in range(n + 2)])

# 검사할 위치(D, U, L, R)
movements = [(1, 0), (-1, 0), (0, -1), (0, 1)]

# 단지 당 집 수를 저장할 리스트
result = []

def bfs(start_row, start_col):
    # 나는 배열을 n + 2 * n + 2 크기로 만들어
    # 인덱스가 배열의 크기를 넘어갔는지 체크할 필요가 없었다.
    # Book-This is coding test에서 음료수 얼려 먹기에서는 매개변수로 넘어온 인덱스가 범위를 넘었는지 체크했다.
    # if start_row < 0 or start_row >= n or start_col < 0 or start_col >= n:
    #     return
    count = 1
    queue = deque()
    queue.append((start_row, start_col))
    # 시작 위치의 값을 그대로 1로 두면 아래 queue 탐색 과정에서 시작점을 한번 더 센다.
    # 따라서 값을 0으로 바꿔준다.
    apartment[start_row][start_col] = 0

    while queue:
        row, col = queue.popleft()
        for movement in movements:
            if apartment[row + movement[0]][col + movement[1]] == 1:
                count += 1
                apartment[row + movement[0]][col + movement[1]] = 0 
                queue.append((row + movement[0], col + movement[1]))
    return count

def check_apart():
    # 단지 수를 저장할 변수
    check = 0
    for row in range(1, n + 1):
        for col in range(1, n + 1):
            if apartment[row][col] == 1:
                check += 1      
                result.append(bfs(row, col))
    result.sort()
    return check
    
print(check_apart())
for i in result:
    print(i)
