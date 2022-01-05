# My Solution(2164ms)
'''
상자(graph)에서 익은 토마토는 1, 익지 않은 토마토는 0, 토마토가 없으면 -1값을 가진다.
이때 익은 토마토가 있는 좌표를 모두 저장하고 해당 좌표들을 이용해 bfs를 수행하면 탐색할 수 있는 모든 0을 확인할 수 있다.
'''
import sys
from collections import deque
input = sys.stdin.readline

m, n = map(int, input().split())                            # m: 열의 길이, n: 행의 길이
graph = [list(map(int, input().split())) for _ in range(n)] # 상자의 정보를 입력받는다.

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

def bfs():
    global result
    q = deque(able_to_start)                                # 큐를 생성하고, 익은 토마토의 좌표를 가지고 있는 able_to_start의 원소를 넣어준다.

    while q:
        x, y = q.popleft()                                  # q의 원소를 꺼낸다.

        for i in range(4):                                  # 모든 방향으로 이동해본다.
            nx = x+dx[i] ; ny = y+dy[i]                     # 다음에 이동할 x, y좌표이다.
            if nx < 0 or nx >= n or ny < 0 or ny >= m:      # 인덱스 범위를 만족하지 않으면 반복문으로 돌아간다.
                continue

            if graph[nx][ny] == 0:                          # 다음에 이동할 좌표가 익지 않은 토마토라면
                graph[nx][ny] = graph[x][y] + 1             # 해당 좌표의 원소값을 갱신한다. (처음 익은 토마토부터 시작해 1씩 더해주기 때문에 지금까지 소요된 시간(일) + 1 값을 가진다.)
                q.append((nx, ny))                          # 좌표를 큐에 넣어주고, result값을 갱신한다.
                result = max(result, graph[nx][ny]-1)       
                

result = 0                                                  # 결과를 저장할 변수다.
able_to_start = []                                          # 시작점으로 삼을 수 있는 좌표를 저장할 리스트다. 익은 토마토가 들어있는 좌표를 넣어주면 된다.
for x in range(n):                                          # 모든 행을 탐색한다.
    for y in range(m):                                      # 모든 열을 탐색한다.
        if graph[x][y] == 1:                                # 익은 토마토라면, able_to_start 리스트에 저장한다.
            able_to_start.append((x, y))

bfs()                                                       # bfs를 수행시켜 result를 갱신한다

# 익지 않은 토마토가 남아있는지 확인하는 함수다.
def check(result):    
    for i in graph:                                         # 상자의 모든 행을 탐색한다.
        if 0 in i: return -1                                # 0이 있다면 -1을 반환한다.
    return result                                           # 0이 없다면 result를 반환한다.

print(check(result))                                        # 결과를 출력한다.

# Other Solution(2216ms)
'''
속도가 더 빠른 코드를 참고해보니 익지 않은 토마토가 남았는지 확인할 때 훨씬 좋은 방법을 사용했다.
익지 않은 토마토의 개수를 미리 세놓는 것이다.
또한 bfs를 수행할 때 내 코드에서는 max() 함수를 이용해 result를 갱신했지만,
사실 graph값이 바뀔 때 result값을 갱신해주면 된다.
예를 들어, graph값이 2인 모든 좌표를 탐색하고 3인 좌표를 탐색하기 전에 result를 갱신하면 된다.

아래 코드를 확인해보자.
'''
import sys
from collections import deque
input = sys.stdin.readline

m, n = map(int, input().split())                                # m: 열의 길이, n: 행의 길이
graph = [list(map(int, input().split())) for _ in range(n)]     # 상자의 정보를 입력받는다.

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

def bfs():
    global result
    global count
    q = deque(able_to_start)                                    # 큐를 생성하고, 익은 토마토의 좌표를 가지고 있는 able_to_start의 원소를 넣어준다.

    while q:
        tmp = len(q)
        for i in range(tmp):
            x, y = q.popleft()                                  # q의 원소를 꺼낸다.
        
            for i in range(4):                                  # 모든 방향으로 이동해본다.
                nx = x+dx[i] ; ny = y+dy[i]                     # 다음에 이동할 x, y좌표이다.
                if nx < 0 or nx >= n or ny < 0 or ny >= m:      # 인덱스 범위를 만족하지 않으면 반복문으로 돌아간다.
                    continue

                if graph[nx][ny] == 0:                          # 다음에 이동할 좌표가 익지 않은 토마토라면
                    graph[nx][ny] = graph[x][y] + 1             # 해당 좌표의 원소값을 갱신한다. (처음 익은 토마토부터 시작해 1씩 더해주기 때문에 지금까지 소요된 시간(일) + 1 값을 가진다.)
                    q.append((nx, ny))                          # 좌표를 큐에 넣어준다.
                    count -= 1                                  # 익지 않은 토마토의 개수를 1 감소시킨다.
        result += 1

result = -1                                                     # 결과를 저장할 변수다.
count = 0
able_to_start = []                                              # 시작점으로 삼을 수 있는 좌표를 저장할 리스트다. 익은 토마토가 들어있는 좌표를 넣어주면 된다.
for x in range(n):                                              # 모든 행을 탐색한다.
    for y in range(m):                                          # 모든 열을 탐색한다.
        if graph[x][y] == 1:                                    # 익은 토마토라면, able_to_start 리스트에 저장한다.
            able_to_start.append((x, y))
        if graph[x][y] == 0:                                    # 익지 않은 토마토의 개수는 미리 세준다.
            count += 1

bfs()                                                           # bfs를 수행시켜 result를 갱신한다

if count:                                                       # 익지 않은 토마토가 남아 있다면 -1을 출력한다.
    print(-1)
else:                                                           # 익지 않은 토마토가 남아있지 않다면 result를 출력한다.
    print(result)
