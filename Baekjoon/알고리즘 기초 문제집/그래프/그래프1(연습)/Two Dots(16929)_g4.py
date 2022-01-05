# My solution1(900ms)
import sys
input = sys.stdin.readline

n, m = map(int, input().split())                        # 게임판 크기 입력, n(행), m(열)
visited = [[False for _ in range(m)] for _ in range(n)] # 방문 확인용 리스트
graph = []                                              # 게임판을 저장할 리스트

for _ in range(n):
    a = list(input().rstrip())
    graph.append(a)

dx = [-1, 1, 0, 0] # 행 방향 u, d, r, l 이동량
dy = [0, 0, 1, -1] # 열 방향 u, d, r, l 이동량

'''
문제의 조건은 아래와 같다.

점 k개 d1, d2, ..., dk로 이루어진 사이클의 정의는 아래와 같다.
1. 모든 k개의 점은 서로 다르다. 
2. k는 4보다 크거나 같다.
3. 모든 점의 색은 같다.
4. 모든 1 ≤ i ≤ k-1에 대해서, di와 di+1은 인접하다. 또, dk와 d1도 인접해야 한다. 두 점이 인접하다는 것은 각각의 점이 들어있는 칸이 변을 공유한다는 의미이다.
게임판의 상태가 주어졌을 때, 사이클이 존재하는지 아닌지 구해보자.

처음에 문제를 읽자마자 사이클이 존재하면 다시 시작점으로 돌아와야 한다고 생각했다.
그래서 그래프를 탐색하면서 시작점으로 다시 돌아오는 순간 k가 4개 이상인지 확인하면 된다고 생각했다.
해당 동작은 dfs함수에서 수행한다.
'''

def dfs(x, y):
    # 이동할 수 있는 곳을 탐색한다.
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        # 배열의 범위를 넘어가면 반복문으로 돌아간다.
        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            continue
        # 그래프의 색이 같다면 이동한다.
        if graph[x][y] == graph[nx][ny]:
            # 방문을 한 번도 하지 않았다면 방문처리를 해준다.
            if not visited[nx][ny]:
                # 해당 위치의 값은 이전 위치에 +1을 한 값이다.
                visited[nx][ny] = visited[x][y] + 1
                if dfs(nx, ny):
                    # dfs의 결과가 True라면 싸이클이 발생한 것이다.
                    # 따라서 동일하게 True를 반환해준다.
                    return True
                visited[nx][ny] = False
                
            # 만약 다음에 이동할 곳이 출발점이라면 사이클이 발생한 것이다.
            if visited[nx][ny] == 1 and visited[x][y] >= 4:
                # 사이클을 발견하면 True를 반환한다.
                return True
    return False

def find():
    for x in range(n):
        for y in range(m):
            visited[x][y] = 1
            if dfs(x, y):
                return 'Yes'
            visited[x][y] = False
    return 'No'

print(find())


# My solution2(80ms)
'''
solution1에서 어떻게 해야 조금더 좋은 코드로 다듬을 수 있을지 생각해봤다.
solution1은 아래와 같은 문제를 가진다.

■■■■
□□■■
위와 같이 사이클이 존재한다고 가정하자.
그러면 1, 2번째 수행에서는 사이클을 찾지 못하고, 3번째 수행에서야 사이클을 찾을 수 있다.
동일한 부분을 dfs하는 과정이 여러번 반복된다는 것이다.

곰곰이 생각해보니 '시작점에 돌아온다.'가 아니라
'이미 탐색한 곳을 다시 돌온다'로 사이클의 정의를 바꾸면 더 빠르게 해결이 가능했다.
그래서 위 코드에서 사이클 발생 조건문만 변경해 주었다.
if visited[nx][ny] == 1 and visited[x][y] >= 4:
    -> if visited[nx][ny] and visited[x][y] - visited[nx][ny] >= 3:
'''
import sys
input = sys.stdin.readline

n, m = map(int, input().split())                       
visited = [[False for _ in range(m)] for _ in range(n)] 
graph = []

for _ in range(n):
    a = list(input().rstrip())
    graph.append(a)

dx = [-1, 1, 0, 0] # 행 방향 u, d, r, l 이동량
dy = [0, 0, 1, -1] # 열 방향 u, d, r, l 이동량

def dfs(x, y):
    # 이동할 수 있는 곳을 탐색한다.
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        # 배열의 범위를 넘어가면 반복문으로 돌아간다.
        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            continue
        # 그래프의 색이 같다면 이동한다.
        if graph[x][y] == graph[nx][ny]:
            # 만약 다음에 이동할 곳이 이미 방문한 곳이라면 사이클이 발생한 것이다.
            # 단, 둘의 차이가 3보다 커야한다.
            if visited[nx][ny] and visited[x][y] - visited[nx][ny] >= 3:
                return True
            
            if not visited[nx][ny]:
                visited[nx][ny] = visited[x][y] + 1
                if dfs(nx, ny):
                    return True
                visited[nx][ny] = False
    return False

def find():
    for x in range(n):
        for y in range(m):
            visited[x][y] = 1
            if dfs(x, y):
                return 'Yes'
            visited[x][y] = False
    return 'No'

print(find())


# My solution3(68ms)
'''
위 방식으로 코드를 수정하고 나니 visited[x][y]를 방문하고 꼭 다시 False로 바꿔야할까? 라는 의문이들었다.
왜냐하면 하나의 색깔 Series를 모두 탐색하고 나면 해당 Series에 사이클이 있는지 없는지는 한 번만 탐색하면 알 수 있다.
즉, 다시 그 Series를 탐색할 이유는 없는 것이다.
따라서 원래 코드에서 사용한 
visited[x][y] = False
코드는 모두 지워주었다.
'''
import sys
input = sys.stdin.readline

n, m = map(int, input().split())                        # 게임판 크기 입력
visited = [[False for _ in range(m)] for _ in range(n)] # 방문 여부 확인

graph = []

for _ in range(n):
    a = list(input().rstrip())
    graph.append(a)

dx = [-1, 1, 0, 0] # 행 방향 u, d, r, l 이동량
dy = [0, 0, 1, -1] # 열 방향 u, d, r, l 이동량

def dfs(x, y):
    # 이동할 수 있는 곳을 탐색한다.
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        # 배열의 범위를 넘어가면 반복문으로 돌아간다.
        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            continue
        # 그래프의 색이 같다면 이동한다.
        if graph[x][y] == graph[nx][ny]:
            # 만약 다음에 이동할 곳이 현재 위치와 이어진다면 사이클이 발생한 것이다.
            # 단, 둘의 차이가 3보다 커야한다.
            if visited[nx][ny] and visited[x][y] - visited[nx][ny] >= 3:
                return True
            
            if not visited[nx][ny]:
                visited[nx][ny] = visited[x][y] + 1
                if dfs(nx, ny):
                    return True
    return False

def find():
    for x in range(n):
        for y in range(m):
            visited[x][y] = 1
            if dfs(x, y):
                return 'Yes'
    return 'No'

print(find())

# Other Solution(80ms)
N,M=map(int,input().split())        # 게임판 크기 입력
L=[input() for i in range(N)]       # 게임판 입력
visited=[[0]*M for i in range(N)]   # 방문 여부 확인
ans=0                               # 정답을 저장할 변수
dx=[1,0,-1,0]                       # 이동 방향(ROW)
dy=[0,1,0,-1]                       # 이동 방향(COL)
def DFS(x,y,depth):
    global ans
    for k in range(4):
        nx,ny=dx[k]+x,dy[k]+y                           # 이동할 위치
        if 0<=nx<N and 0<=ny<M and L[x][y]==L[nx][ny]:  # 인덱스 범위에 속하고, 색이 같으면 조건문 실행
            if visited[nx][ny]==0:                      # nx, ny를 방문하지 않았다면 방문한다.
                visited[nx][ny]=depth+1                 # x, y의 값이 depth에 1을 더한 값으로 지정한다.
                DFS(nx,ny,depth+1)                      # DFS를 실행한다.
            else:                                       # nx, ny를 이미 방문했다면
                r=depth-visited[nx][ny]                 # r을 구한다
                if ans<r: ans=r                         # ans가 r보다 작다면 r을 대입한다.

# 모든 위치에 DFS를 실행한다.
for i in range(N):
    for j in range(M):        
        if visited[i][j]==0:    # 방문하지 않았다면 조건문을 실행한다.
            visited[i][j]=1     # 처음 위치이므로 해당 위치에 1을 대입한다.
            DFS(i,j,1)          # DFS를 실행한다.
if ans>=3: print('Yes')         # 모든 DFS를 실행한 후의 결과가 3보다 크다면 Yes를 출력한다.
else: print('No')               # 아니라면 No를 출력한다.