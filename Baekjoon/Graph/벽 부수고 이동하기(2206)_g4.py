# My Solution(4120ms)
import sys
from collections import deque
input = sys.stdin.readline
'''
벽을 한 번 깨는 것이 가능하며, n, m위치에 도달하는데 가능한 최단 거리를 구해야 한다.
일반적으로 최단거리는 bfs가 편하므로 bfs를 사용했다.
단, 큐에 위치(x, y)뿐만 아니라 벽을 깬 횟수, 지금까지 거친 경로를 저장하도록 했다.
그리고 벽을 깼을 때 해당 위치의 방문 여부, 벽을 깨지 않았을 때 해당 위치의 방문 여부를 따로 표시해줬다.
이유는 벽을 깨지 않으면서 이동했을 때와, 벽을 깨고 이동했을 때의 최단거리가 달라질 수 있기 때문이다.
'''
n, m = map(int, input().split())
graph = []

for _ in range(n):
    graph.append(list(map(int, list(input().rstrip()))))

dx = [-1, 1, 0, 0] # u, d, r, l
dy = [0, 0, 1, -1] # u, d, r, l

visited1 = [[False for _ in range(m)] for _ in range(n)]
visited2 = [[False for _ in range(m)] for _ in range(n)]
def bfs():
    visited1[0][0] = True
    q = deque([(0, 0, 0, 1)])                           # x, y, 벽을 깬 횟수(최대 1), 지금까지 경로
    
    while q:
        x, y, count, path = q.popleft()                 # 큐에서 원소하나를 꺼낸다.
        if x == n-1 and y == m-1:                       # 도착지점에 도착했다면 path를 출력한다. bfs이므로 가장 먼저 해당 위치를 반환하는 path가 정답이다.
            return path
        
        for i in range(4):
            nx = x+dx[i]                    
            ny = y+dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= m:  # 이동할 위치가 범위 밖이면 반복문으로 돌아간다.
                continue
            
            if graph[nx][ny] == 0 and count == 0:       # 이동할 위치가 벽이 아니고 지금까지 벽을 깬 적이 없다면
                if not visited1[nx][ny]:                # 지금까지 방문한 적이 있다면 벽을 깨지 않고 갔을 때의 최단거리가 이미 정해진 지점이므로 방문한 적이 있는지 체크한다.
                    visited1[nx][ny] = True             # 방문처리를 해준다.
                    q.append((nx, ny, count, path+1))   # 해당 위치를 큐에 넣어준다.
            
            if graph[nx][ny] == 0 and count == 1:       # 이동할 위치가 벽이 아니고 지금까지 벽을 깬 적이 있다면
                if not visited2[nx][ny]:                # 지금까지 방문한 적이 있다면 벽을 깨고 갔을 때의 최단거리가 이미 정해진 지점이다. 따라서 방문 여부를 체크한다.
                    visited2[nx][ny] = True             # 방문처리를 해준다.
                    q.append((nx, ny, count, path+1))   # 해당 위치를 큐에 넣어준다.
                
            if graph[nx][ny] == 1 and count == 0:       # 이동할 위치가 벽이고 지금까지 벽을 깬적이 없다면 (벽을 깬적이 있다면 지나갈 수 없다)
                if not visited2[nx][ny]:                # 해당 벽을 지나간 적이 있다면 이미 최단거리가 정해진 지점이다. 따라서 방문 여부를 체크한다.
                    visited2[nx][ny] = True             # 방문처리를 해준다.
                    q.append((nx, ny, 1, path+1))       # 해당 위치를 큐에 넣어준다.
    return -1

print(bfs())

'''
해당 코드는 잘 돌아가지만 단점이 있다.
visited2의 경우 필요없는 연산을 하게 된다.
즉, 벽이 발견되고 조건문을 실행하면 이전에 방문했던 위치는 방문처리가 되어 있지 않아 다시 탐색해야 한다.
'''

# Other Solution(5616ms)
import sys
from collections import deque
input = sys.stdin.readline
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]
def bfs():
    q = deque()
    q.append([0, 0, 1])
    '''
    아래와 같이 visited1과 visited2를 합친 형태로 리스트를 작성하니 반복문 안에서 조건식을 줄일 수 있었다.
    참고하면 좋을 것 같다.
    '''
    visit = [[[0] * 2 for i in range(m)] for i in range(n)] # 내 코드에서 visited1과 visited2를 합쳐놓은 리스트이다.  
    visit[0][0][1] = 1                                      # 벽을 한 번도 깨지 않은 경우의 0, 0위치에 방문 처리를 한다.
    while q:
        a, b, w = q.popleft()
        if a == n - 1 and b == m - 1:                       # 도착지점에 가장 빨리 도착한 결과를 반환한다.
            return visit[a][b][w]                           
        for i in range(4):
            x = a + dx[i]
            y = b + dy[i]
            if 0 <= x < n and 0 <= y < m:                   # 이동할 위치가 범위 이내이면 아래 코드를 실행한다.
                if s[x][y] == 1 and w == 1:                 # 벽을 한 번도 깨지 않았고 다음에 이동할 위치가 벽이라면 => 이동한 적이 있는 벽인지 체크했다면 시간이 줄었을 것 같다.(4644ms로 1000ms 정도 줄었다.)
                    visit[x][y][0] = visit[a][b][1] + 1     # 이전 값에 +1을 한 값을 해당 위치에 넣어준다.
                    q.append([x, y, 0])
                elif s[x][y] == 0 and visit[x][y][w] == 0:  # 이동할 위치가 벽이 아니고 방문한 적이 없다면
                    visit[x][y][w] = visit[a][b][w] + 1     # 이전 값에 +1을 한 값을 해당 위치에 넣어준다.
                    q.append([x, y, w])                     
    return -1

n, m = map(int, input().split())
s = []
for i in range(n):
    s.append(list(map(int, list(input().strip()))))
print(bfs())

# 출처: https://pacific-ocean.tistory.com/348