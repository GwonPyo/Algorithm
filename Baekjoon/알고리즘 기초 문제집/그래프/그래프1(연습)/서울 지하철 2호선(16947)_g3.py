# My Solution(1360ms)
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n = int(input())                                                # 역의 개수(=간선의 개수)를 입력받는다, 3 ≤ N ≤ 3,000
visited = [False for _ in range(n+1)]                           # 방문 여부를 확인할 리스트를 생성한다.
graph = [[] for _ in range(n+1)]                                # graph를 저장할 리스트를 생성한다.

for _ in range(n):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(now, visited, graph):
    for i in graph[now]:
        # 출발점을 돌아온 경우 True를 리턴한다. 단, 최소 2개의 간선을 거쳐서 도달해야 한다(그래야 cycle이 만들어지기 때문이다.).
        if visited[i] == 1 and visited[now] - visited[i] >= 2:
            return True
        if not visited[i]:                                      # 이전에 방문한 노드가 아니라면
            visited[i] = visited[now] + 1                       # 이전 노드에 +1한 값을 넣어준다.
            if dfs(i, visited, graph):                          # dfs를 시도하고 cycle이 발생했다면
                visited[i] = 1                                  # 해당 노드의 값을 1로 설정한다.
                return True
            visited[i] = False                                  # cycle이 발생하지 않았다면 False를 대입한다.
    return False                                                # 연결된 모든 노드를 탐색했는데 cycle이 발생하지 않았다면 False를 리턴한다.
            
def dfs2(now, visited, graph):
    for i in graph[now]:                                        # 현재 노드와 연결된 노드들을 탐색한다.            
        if visited[i] > visited[now]:                           # cycle에 포함되지 않은 곳은 3000이 저장되어 있다. 따라서 현재 노드보다 무조건 값이 크므로 값이 크다면 해당 조건문을 실행한다.
            visited[i] = visited[now] + 1                       # 현재 노드값에 +1한 값을 저장한다.
            dfs2(i, visited, graph)                             # dfs 탐색을 시켜준다.

for i in range(1, n+1):                                         # 1~n+1까지 모든 노드를 돌면 cycle을 판별한다.
    if not visited[i]:                                          # 노드를 방문하지 않았다면
        visited[i] = 1                                          # 노드의 값을 1로 설정한다.(처음 값이므로)
        if dfs(i, visited, graph): break                        # dfs를 시켜주고 사이클이 발견되는지 확인한다. 사이클이 발생되었다면 반복문을 종료한다.
        visited[i] = False                                      # cycle이 발견되지 않았다면 반복문으로 돌아간다.(시간이 오래 걸리는 원인같다.)

for i in range(1, n+1):                                         # cycle에 포함되지 않은 값들에 3000을 넣어준다. (3000은 될 수 없는 값이기 때문이다.)
    if not visited[i]:
        visited[i] = 3000

for i in range(1, n+1):                                         # visited가 1인 곳은 cycle에 포함되어 있는 노드이다. 따라서 각 노드마다 확인되지 않은 노드를 탐색해준다.
    if visited[i] == 1:
        dfs2(i, visited, graph)

for i in range(1, n+1):                                         # 결과를 출력한다.
    print(visited[i]-1, end = ' ')

# Other Solution(96ms)
import sys
from collections import deque
sys.setrecursionlimit(10**6)

def dfs(node, past):
    if chk[node] == 1:              # 이전에 탐색한 node로 돌아온다면 node를 리턴한다.
        '''
        지금까지 탐색된 node들은 모두 1이 저장되어 있다.
        그리고 바로 직전 노드는 
        if nxt == past: continue
        로 차단되므로 node를 리턴해도 문제가 없다.
        내 코드처럼 True혹은 False를 리턴해 cycle을 판별하면 cycle이 아닌 곳에서 탐색하는 경우 여러 번 dfs를 수행해야하는 문제가 생긴다.
        아래와 같이 node를 반환하고 node에 도달했는지 확인하여 cycle을 판별한다면 dfs를 한 번만 쓰고 cycle을 판별할 수 있다.
        '''
        return node
    
    chk[node] = 1                   # 인자로 들어온 node를 1로 초기화한다.

    for nxt in adj[node]:           # node와 연결된 nxt를 탐색한다.
        if nxt == past:             # nxt가 이전 node와 동일하면 반복문으로 돌아간다. 
            continue    
        res = dfs(nxt, node)        # dfs(nxt, node)를 실행한 결과를 res에 저장한다. (-1을 리턴한 경우 아무것도 하지 않는다.)
        
        '''
        해당 노드와 연결된 다른 노드를 모두 탐색했을 때 cycle이 없다면 -1을 리턴한다.
        해당 리턴을 받으면 반복문으로 돌아가 다른 연결된 노드가 있는지 확인해야한다.
        따라서 res를 -2가 아닌 -1로 반환하면 문제가 생긴다. 
        '''
        if res == -2:               # 만약 dfs의 결과가 -2라면, -2를 리턴한다.
            return -2
        if res >= 0:                # dfs결과가 0보다 크다면
            chk[node] = 2           # cycle내에 있는 node의 값은 2로 설정한다.
            '''
            res값과 node값이 같아지면 cycle한번을 완료한 것이다. cycle이 끝났으므로 나머지는 0이 아닌 값을 가진다.
            그래서 2가 아닌 -2값을 return해준다. 밑에 코드를 보면 -2값을 가진 node들이 하는 일은 아무것도 없다. 
            이를 통해 한 번의 dfs로 cycle에 있는 원소들을 알 수 있어 시간을 절약할 수 있다. -2로 지정하는 이유는 위와 동일하다.
            '''
            if node == res:         # node가 dfs의 결과와 같다면 
                return -2           # -2를 리턴한다.
            else:                   # node가 dfs의 결과와 다르다면
                return res          # res를 리턴한다.
    return -1


input = sys.stdin.readline
N = int(input())                    # 역 개수(역의 개수는 간선의 개수와 동일하다.)
adj = [[] for _ in range(N + 1)]    # graph를 저장할 리스트
chk = [False] * (N + 1)             # 노드의 위치를 저장할 리스트

for i in range(N):
    s1, s2 = map(int, input().split())
    adj[s1].append(s2)
    adj[s2].append(s1)

dfs(1, 0)                           # 시작 node는 1, 이전 node는 0으로 설정하고 탐색한다.
queue = deque()                 
res = [-1] * (N + 1)                # 결과값을 저장할 리스트다.
for i in range(1, N + 1):
    if chk[i] == 2:                 # chk[i]에 2가 저장되어 있다면 cycle안에 있는 node이다.
        res[i] = 0                  # res[i]에 0을 저장한다.
        queue.append(i)             # i를 queue에 넣는다.

while queue:
    node = queue.popleft()          
    for nxt in adj[node]:           # queue에서 빼낸 node와 연결된 노드를 찾는다.
        if res[nxt] == -1:          # 아직 결과값이 -1인 노드는 cycle 밖에 있는 노드이므로 아래 코드를 실행해준다.
            res[nxt] = res[node] + 1# 해당 노드의 값은 이전 node에 +1을한 값이다.
            queue.append(nxt)       # queue에 해당 노드를 넣어준다.

print(' '.join(map(str, res[1:])))

'''
내 코드는 하나의 사이클에 포함된 node가 아니라면 cycle을 찾기 위해 여러번의 dfs를 수행해야 했다.
하지만 위처럼 어느 하나의 값으로 cycle에 포함된 node들을 표시해 한 번의 dfs만으로 cycle을 판별할 수 있는 방식은 꼭 알아놓는 것이 좋을 것 같다.
또한 dfs를 사용하고 bfs를 한 번더 사용하는 방식의 문제는 처음 접해봤다.
이런 문제들도 익숙해질 필요가 있을 것 같다.
'''

# My solution + Other Solution(100ms)
# 내 코드를 위 코드를 참고해 개선해보았다.

import sys
from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n = int(input())
visited = [False for _ in range(n+1)]
dist = [0 for _ in range(n + 1)]
graph = [[] for _ in range(n+1)]
for _ in range(n):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(now):
    visited[now] = 1
    for i in graph[now]:
        if visited[i] == 1 and dist[now] - dist[i] >= 2:
            visited[i] = 2              # 해당 코드를 실행하지 않으면 visited[i]의 값은 -2로 설정된다.                      
            return i
        if not visited[i]:
            dist[i] = dist[now] + 1
            result = dfs(i)
            if result == -2:
                return -2
            if result > 0:
                visited[i] = 2
                if now == result:
                    return -2
                else:
                    return result
    return -1

dist[1] = 1
dfs(1)
q = deque()
result = [-1 for _ in range(n + 1)]
for i in range(1, n+1):
    if visited[i] == 2:
        result[i] = 0
        q.append(i)
        
def bfs():
    while q:
        now = q.popleft()
        for i in graph[now]:
            if result[i] == -1:
                result[i] = result[now] + 1
                q.append(i)

bfs()
print(' '.join(map(str, result[1:])))
        
