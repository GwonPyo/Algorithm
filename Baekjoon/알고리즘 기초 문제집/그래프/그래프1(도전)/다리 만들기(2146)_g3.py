# My Solution(1708ms)
'''
아래 코드를 요약하자면 다음과 같다.
1. 섬 하나를 지정해 bfs로 탐색한다.
2. 섬 주변의 바다들을 큐에 넣어준다.
3. 다시 bfs로 큐에 저장된 바다 좌표들을 이용해 다른 섬까지 가는데 필요한 다리의 최소 길이를 구해준다.
4. 해당 값이 result보다 작으면 result값을 갱신한다.
'''
import sys
from collections import deque
input = sys.stdin.readline
INF = int(1e9)

n = int(input())                                                    # 지도의 크기를 입력받는다.
graph = [list(map(int, input().split())) for _ in range(n)]         # 지도를 입력받는다.

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

result = INF
def bfs(x, y):
    global result
    '''
    임의의 좌표에 건설할 수 있는 다리의 최단 길이를 visitedited에 저장할 것이다.
    탐색을 시작한 섬의 모든 좌표는 탐색 후 확인할 필요가 없으므로 graph의 원소값을 -1로 지정할 것이다.
    중요한 점은 graph의 값이 1인 지점(육지)에는 -1값을 저장한다는 점과 
    주변에 값이 0인 지점(바다)는 이후 다리의 출발 지점이 되므로 리스트에 해당 좌표들을 모두 저장해 놓는다는 점이다. (tmp_list에 저장한다.)
    '''
    visited = [[INF for _ in range(n)] for _ in range(n)]           # 각 좌표에서 지을 수 있는 다리의 최소한의 길이를 저장할 리스트다.
    
    q = deque()                                                     # 모든 원소값을 -1로 지정하기 위해 사용할 큐이다.
    tmp_list = []                                                   # 해당 섬 주변에서 다리를 시작할 수 있는 지점(값이 0인 지점 / 바다인 지점)의 좌표값을 찾아 저장할 것이다.
    q.append((x, y))                                                # 시작 좌표를 큐에 넣어준다.
    graph[x][y] = -1                                                # 현재 좌표의 graph 값을 -1로 갱신한다.
    visited[x][y] = 0                                               # visited[x][y]의 값을 0으로 갱신한다. (다리를 아직 짓지 않아도 되기 때문이다.)
    while q:
        x, y = q.popleft()                                          # 탐색할 좌표를 꺼낸다.

        for i in range(4):
            nx = x+dx[i]; ny = y+dy[i]                              # 다음 위치의 x, y좌표를 저장한다. 
            if nx < 0 or nx >= n or ny < 0 or ny >= n:              # 인덱스 범위에 벗어난다면, 반복문으로 돌아간다.
                continue

            if graph[nx][ny] == 1:                                  # 다음 지점이 육지라면
                q.append((nx, ny))                                  # 탐색해야 하므로 큐에 추가한다.
                graph[nx][ny] = -1                                  # graph의 값은 1로 갱신하고, 다리는 아직 놓을 필요가 없으므로 visited 값은 0으로 지정한다.
                visited[nx][ny] = 0

            elif graph[nx][ny] == 0:                                # 다음 지점이 바다라면
                tmp_list.append((nx, ny))                           # 현재 반복문에서는 바다는 탐색할 필요가 없으므로 큐에 추가할 필요는 없고, 이후에 사용하기 위해 tmp_list에 저장한다.
                visited[nx][ny] = 1                                 # 다리가 시작되는 지점이므로 visitedited를 1로 지정한다.
    
    '''
    bfs로 탐색하므로 가장 먼저 육지(값이 1인 좌표)에 도달하면 해당 다리가 가장 짧게 설치할 수 있는 다리가 된다.
    주의할 점은 어떠한 좌표를 이미 방문했다면 해당 좌표의 최단 거리는 이미 정해졌다는 것이다.
    '''
    q = deque(tmp_list)                                             # 출발점으로 삼을 수 있는 좌표들이 담긴 tmp_list를 큐로 만든다.
    while q:
        x, y = q.popleft()                                          # 탐색할 좌표를 꺼낸다.

        for i in range(4):
            nx = x+dx[i]; ny = y+dy[i]                              # 다음 위치의 x, y좌표를 저장한다. 
            if nx < 0 or nx >= n or ny < 0 or ny >= n:              # 인덱스 범위에 벗어난다면, 반복문으로 돌아간다.
                continue

            if visited[nx][ny] == INF and graph[nx][ny] == 0:       # 해당 좌표를 방문한 적이 없고, 다리를 놓아야하는 지점이라면
                visited[nx][ny] = visited[x][y]+1                   # visited[nx][ny]에는 다리 한 칸을 추가한 값인 visited[x][y]+1로 지정한다.
                q.append((nx, ny))                                  # 큐에 해당 좌표를 넣어준다.
                
            elif graph[nx][ny] == 1:                                # 섬에 도달해 다리가 끝나는 지점이라면
                result = min(result, visited[x][y])                 # 지금까지 결과중 최소값과 비교해 더 작은 값을 result에 정한다.
                return                                              # 더 탐색할 필요가 없으므로 함수를 종료한다.
            
for x in range(n):
    for y in range(n):
        if graph[x][y] == 1:
            bfs(x, y)

print(result)

# Other Solution1(3412ms)
# 출처: https://kyun2da.github.io/2021/04/22/makeBridge/
'''
모든 지점을 탐색해보는 코드이다. 아래와 같은 과정으로 진행된다.
1. 모든 원소를 탐색하면서 각 섬마다 번호를 매긴다. (해당 과정은 bfs1 함수로 수행된다.)
2. 이후 각 섬마다 bfs2 함수를 수행한다. bfs2는 다음과 같은 과정으로 진행된다.
   - graph의 모든 원소를 탐색하면서 현재 섬의 모든 원소를 큐에 저장한다.
   - 모든 원소를 저장했다면, 큐의 원소를 하나씩 꺼낸다.
    다음에 이동할 곳이 0이라면 현재까지의 최소값 + 1을 저장하고 다른 섬에 도착한다면 result를 갱신한다.
'''
import sys
from collections import deque
input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


'''
bfs로 섬의 시작점부터 탐색하면서
해당 섬의 모든 좌표들의 graph값을 섬의 번호(number)로 지정한다.
'''
def bfs1(i, j):                                          
    q = deque()                                                 # 큐를 생성하고, 섬이 시작하는 좌표를 넣어준다.
    q.append([i, j])
    visited[i][j] = True                                        # 해당 좌표를 방문 처리해주고, 섬의 번호를 넣어준다.
    graph[i][j] = number

    while q:                                                
        x, y = q.popleft()                                      # 큐에 들어있는 좌표를 꺼내고 탐색한다.
        for k in range(4):
            nx = x + dx[k]                                      # 다음에 이동할 x좌표이다.
            ny = y + dy[k]                                      # 다음에 이동할 y좌표이다.
            if nx < 0 or nx >= n or ny < 0 or ny >= n:          # 좌표가 인덱스 범위를 넘어가면, 반복문으로 돌아간다.
                continue
            
            if not visited[nx][ny] and graph[nx][ny] == 1:      # 해당 좌표를 방문한 적이 없고, 섬이라면(값이 1이라면)
                visited[nx][ny] = True                          # 방문 처리를 해주고, 섬의 번호로 값을 갱신한다.
                graph[nx][ny] = number
                q.append([nx, ny])                              # 큐에 해당 좌표를 넣어준다.


'''
모든 섬을 탐색하면서 해당 섬에서 다른 임의의 섬으로 가는데 필요한 최소한의 다리 길이를 구한다.
탐색할 섬의 모든 좌표를 큐에 넣어주고
다음에 이동할 곳이 바다라면(0)이라면 이동하고
다음에 이동할 곳이 다른 섬이라면(count가 다르다면 / 좌표끼리의 graph값이 다르다면) result와 비교해 더 작은값으로 result를 갱신한다.
'''
def bfs2(count):
    global result                                               # result를 global 변수로 지정한다.
    dist = [[-1] * n for _ in range(n)]                         # 해당 좌표에서 다리의 최단 길이를 저장할 리스트다
    q = deque()                     

    for i in range(n):                                          # 모든 행을 탐색한다.
        for j in range(n):                                      # 모든 열을 탐색한다.
            if graph[i][j] == count:                            # 만약 해당 좌표가 탐색하려는 섬이라면
                q.append([i, j])                                # 큐에 저장하고, dist값을 0으로 지정한다.
                dist[i][j] = 0

    while q:
        x, y = q.popleft()                                      # 큐에 들어있는 좌표를 꺼낸다.
        for i in range(4):          
            nx = x + dx[i]                                      # 다음에 이동할 x좌표이다.
            ny = y + dy[i]                                      # 다음에 이동할 y좌표이다.
            if nx < 0 or nx >= n or ny < 0 or ny >= n:          # 좌표가 인덱스 범위를 넘어가면, 반복문으로 돌아간다.
                continue

            if graph[nx][ny] > 0 and graph[nx][ny] != count:    # 다른 섬에 도달했다면
                result = min(result, dist[x][y])                # answer값을 갱신하고 함수를 종료한다.
                return
            
            if graph[nx][ny] == 0 and dist[nx][ny] == -1:       # 해당 좌표가 바다고, 처음 방문했다면
                dist[nx][ny] = dist[x][y] + 1                   # 현재 좌표의 dist보다 1을 더한값을 dist값으로 지정한다.
                q.append([nx, ny])                              # 큐에 해당 좌표를 추가한다.


n = int(input())                                                # 지도 크기를 입력받는다.

graph = [list(map(int, input().split())) for _ in range(n)]     # 지도를 입력받는다.
visited = [[False] * n for _ in range(n)]                       # 각 좌표의 방문 여부를 체크할 리스트다.
number = 1                                                      # 섬의 개수+1을 저장할 변수다.
result = sys.maxsize                                        

for i in range(n):                                              # 모든 행을 탐색한다.
    for j in range(n):                                          # 모든 열을 탐색한다.
        if not visited[i][j] and graph[i][j] == 1:              # 해당 위치를 방문한 적이 없고, 육지라면
            bfs1(i, j)                                          # bfs1을 수행한다.
            number += 1                                         # number를 갱신한다.


for i in range(1, number):                                      # 섬의 개수만큼 bfs2를 수행한다.
    bfs2(i)

print(result)

# Other Solutioin2(104ms)
'''
실제로 정답인 코드를 가져왔지만 해당 코드는 정답이 아니다.
반례는 아래와 같다.
(입력)
5
1 0 0 0 1
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0
1 1 0 0 1
(출력) 3
(정답) 2

아래 코드는 다음과 같은 과정으로 진행된다. (V의 값을 의미한다.)
0 1 0 1 0
1 0 0 0 1
0 0 0 0 0
1 1 0 0 1
0 0 1 1 0

0 1 2 1 0
1 2 0 0 1
2 0 0 0 0
1 1 0 0 1
0 0 1 1 0

위는 첫 번째 섬의 주변 원소를 탐색한 이후의 v리스트 상태다.
다음에는 두 번째 섬의 주변 원소를 탐색해야 하는데 이미 2와 1이 만나서 답은 3이 된다.
하지만 아래에 세 번재와 네 번째 섬을 이어서 길이가 2인 다리를 만들 수 있다.
이와 같은 반례로 인해 해당 코드는 정확하지 않다.
이를 보완해서 내 코드로 재작성해 보았다.
'''
import sys
sys.setrecursionlimit(10**6)

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def island(x, y):
    global rear
    for i in range(4):
        nx = x + dx[i]                                                  # 다음에 이동할 x좌표다.
        ny = y + dy[i]                                                  # 다음에 이동할 y좌표다.
        if 0 <= nx < N and 0 <= ny < N:                                 # 좌표가 인덱스 범위를 만족한다면                        
            if graph[nx][ny] == 1:                                      # 다음 위치가 육지라면(값이 1이라면)
                graph[nx][ny] = graph[x][y]                             # 현재 좌표와 동일한 값으로 지정해준다.
                island(nx, ny)                                          # 다음 위치에 동일한 과정을 수행한다.(dfs)
            elif graph[nx][ny] == 0:                                    # 다음 위치가 바다라면(값이 0이라면)
                graph[nx][ny] = graph[x][y]                             # 현재 좌표와 동일한 값으로 지정해준다.
                rear += 1                                               # rear값을 갱신한다.
                Q[rear] = (nx, ny, 1)                                   # Q의 rear번째 인덱스에 좌표, 다리의 길이를 입력한다.
                V[nx][ny] = 1                                           # 다리의 길이는 1이므로 V값에 1을 넣어준다.
                
            elif graph[nx][ny] < 0 and graph[nx][ny] != graph[x][y]:    # 다음 위치가 다음 섬이라면 해당 좌표는 이전에 탐색하면서 바다부분을 다른 섬의 번호로 바꿔준 좌표일 것이다.
                global result                                           # 따라서 길이가 1인 다리로 섬을 이을수 있다는 것이기 때문에 answer을 1로 지정한다.
                result = 1
                

def BFS(x, y, n):
    global rear, result                                                 # rear와 answer을 global 변수로 지정한다.
    for i in range(4):
        nx = x + dx[i]                                                  # 다음에 이동할 x좌표이다.
        ny = y + dy[i]                                                  # 다음에 이동할 y좌표이다.
        if 0 <= nx < N and 0 <= ny < N:                                 # 좌표가 인덱스 범위를 만족한다면
            if graph[nx][ny] == 0:                                      # 다음 위치가 바다라면(값이 0이라면)
                graph[nx][ny] = graph[x][y]                             # graph[nx][ny]를 현재 위치의 섬 번호(graph[x][y])로 지정한다.
                V[nx][ny] = n+1                                         # V값에는 이전 다리값인 n+1을 넣어준다.
                rear += 1                                               # rear에 1을 더해주고 해당 인덱스의 Q원소에 해당 좌표와 다리 길이(n+1)를 넣어준다.
                Q[rear] = (nx, ny, n+1)
            elif graph[nx][ny] != graph[x][y]:                          # 만약 다른 섬에 해당하는 지점을 만났다면 answer를 갱신한다. 이후 answer을 더 탐색할 필요는 없다.  
                result = V[nx][ny] + V[x][y]

                


N = int(input())                                                        # 지도의 크기를 입력받는다.         
graph = [list(map(int, input().split())) for _ in range(N)]             # 지도를 입력받는다.

Q = [0] * N * N                                                         # 원소(좌표)의 개수만큼의 크기를 가진 리스트를 생성한다. (탐색해야 하는 좌표와 현재까지의 최소 길이를 담을 리스트이다.)                                
front = -1                                                              # 이후 Q의 원소를 탐색할 때 사용할 변수다.(Q의 인덱스로 활용할 것이다.)
rear = -1                                                               # 다음 원소를 저장할 수 있는 Q의 인덱스를 의미한다.
V = [[0]*N for _ in range(N)]                                           # 좌표마다 지을 수 있는 다리의 최소 길이를 저장할 리스트이다.
result = 0                                                              # 결과를 저장할 변수이다.
cnt = 0                                                                 # 섬의 번호를 의미하는 변수다.
for x in range(N):                                                      # 모든 행과 열을 탐색한다.
    for y in range(N):
        if graph[x][y] == 1:                                            # 해당 좌표가 섬이라면
            cnt -= 1                                                    # 번호를 갱신한다.
            graph[x][y] = cnt                                           # 해당 좌표의 graph값을 섬의 고유 번호로 지정한다.
            island(x, y)    

while result == 0:                                                      # result값이 갱신될 때까지 반복한다.
    front +=1                                                           
    BFS(Q[front][0], Q[front][1], Q[front][2])                          # Q의 원소들을 꺼내 탐색한다. 

print(result)

# Improved Other Solution2(112ms)
'''
해당 코드가 진행되는 예시를 들어보자.

(입력)
5
1 0 0 0 1
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0
1 1 0 0 1

(처음 bfs과정/check_island 함수)
graph 값
-1 -1  0 -2 -2
-1  0  0  0 -2
 0  0  0  0  0
-3 -3  0  0 -4
-3 -3 -3 -4 -4
visited 값
0 1 0 1 0
1 0 0 0 1
0 0 0 0 0
1 1 0 0 1
0 0 1 1 0

(두 번째 bfs 과정)
graph 값
-1 -1 -1 -2 -2
-1 -1  0 -2 -2
-1 -3  0  0 -4
-3 -3 -3 -4 -4
-3 -3 -3 -4 -4

visited 값
0 1 2 1 0
1 2 0 2 1
2 2 0 0 2 
1 1 2 2 1
0 0 1 1 0

이전 코드에서 발생한 반례의 문제는 순서상 2와 1이 먼저 더해졌기 때문이다.
이는 다리의 길이가 1인 모든 좌표를 탐색하고 result를 갱신해 준다면 해결할 수 있다.
따라서 2+1 이후에도 1+1을 수행할 수 있으므로 2를 출력한다.
아래 코드에서는 탐색할 좌표의 visited값이 ex_length와 달라지고 result값이 INF가 아니라면 탐색을 멈춘다.
'''
import sys
from collections import deque
input = sys.stdin.readline
INF = int(1e9)

n = int(input())                                                        # 지도의 크기를 입력받는다.
graph = [list(map(int, input().split())) for _ in range(n)]             # 지도를 입력받는다.

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
 
def check_island(x, y):
    global result
    q = deque()                                                         # 큐를 생성한다.                                
    q.append((x, y))                                                    # 시작 좌표를 큐에 넣어준다.
    graph[x][y] = label                                                 # 현재 좌표의 graph값을 label값으로 갱신한다. 

    while q:
        x, y = q.popleft()                                              # 탐색할 좌표를 꺼낸다.

        for i in range(4):
            nx = x+dx[i]; ny = y+dy[i]                                  # 다음 위치의 x, y좌표를 저장한다. 
            if nx < 0 or nx >= n or ny < 0 or ny >= n:                  # 인덱스 범위에 벗어난다면, 반복문으로 돌아간다.
                continue

            if graph[nx][ny] == 1:                                      # 다음 지점이 육지라면
                graph[nx][ny] = label                                   # graph값은 label값으로 갱신하고, 다리는 아직 놓을 필요가 없으므로 visited값은 0으로 지정한다.
                q.append((nx, ny))                                      # 탐색해야 하므로 큐에 추가한다.
            
            elif graph[nx][ny] == 0:                                    # 다음 지점이 바다라면           
                graph[nx][ny] = label                                   # graph값은 label값으로 갱신하고 다리가 시작되는 지점이므로 visited값은 1로 지정한다.
                visited[nx][ny] = 1                                 
                able_to_start.append((nx, ny))                          # 이후에 다리의 출발점이 되므로 리스트에 저장해 놓는다.

def bfs():
    global result
    q = deque(able_to_start)                                            # 큐를 생성한다.
    ex_length = 1                                                       # 탐색하는 다리의 길이가 바뀌었는지 확인하기 위해 만들어준 변수다.
    while q:
        x, y = q.popleft()                                              # 큐의 원소를 꺼낸다.
        if ex_length != visited[x][y]:                                  # 만약 탐색하는 다리의 길이가 바뀌었고
            if result == INF: ex_length = visited[x][y]                 # result값이 아직 갱신되지 않았다면 ex_length를 탐색할 다리의 길이로 갱신해준다.
            else: return                                                # result값이 갱신되었다면 함수를 종료한다.
            
        for i in range(4):
            nx = x+dx[i]; ny = y+dy[i]                                  # 다음 위치의 x, y좌표를 저장한다. 
            if nx < 0 or nx >= n or ny < 0 or ny >= n:                  # 인덱스 범위에 벗어난다면, 반복문으로 돌아간다.
                continue

            if graph[nx][ny] == 0:                                      # 다음 지점이 바다라면(graph 값이 0이라면)
                graph[nx][ny] = graph[x][y]                             # 해당 좌표의 값을 graph[x][y]로 지정한다.(x, y의 섬 label값이다.)
                visited[nx][ny] = visited[x][y]+1                       # 다리의 길이는 이전값에서 1을 더한 값이어야 한다. 따라서 visited[x][y]에 1을 더한 값으로 지정한다.
                q.append((nx, ny))                                      # 해당 좌표는 이후에 탐색해야 하므로 큐에 넣어준다.
                

            elif graph[nx][ny] != graph[x][y]:                          # 다음 지점이 다른 섬이라면
                result = min(result, visited[x][y] + visited[nx][ny])   # result값과 비교해 더 작은 값으로 result를 갱신한다.

    
label = -1                                                              # 섬의 번호를 의미하는 변수다.
result = INF                                                            # 결과를 저장할 변수다.
visited = [[0 for _ in range(n)] for _ in range(n)]                     # 좌표마다 지을 수 있는 최소한의 다리 길이를 저장할 리스트다.
able_to_start = []                                                      # 출발점으로 삼을 수 있는 좌표를 저장할 것이다. bfs() 함수에서 큐를 만들때 사용된다.

for x in range(n):                                                      # 모든 행과 열을 탐색한다.
    for y in range(n):
        if graph[x][y] == 1:                                            # 해당 좌표가 섬이라면(graph값이 1이라면)
            check_island(x, y)                                          # 해당 섬의 모든 원소와 주변 바다의 graph값을 label값으로 갱신하고, able_to_start에 주변 바다의 좌표를 넣어준다.
            label -= 1                                                  # 다른 섬들은 다른 label로 설정해야 하므로 label에 1을 뺀값을 저장한다.

bfs()                                                                   # bfs() 함수를 수행하고 결과를 출력한다.
print(result)