# My solution1(오답)
import sys
input = sys.stdin.readline

'''
group_a, group_b 두 개의 group을 만들고 해당 리스트들은 bool type을 가지도록 했다.
그리고 원소값이 True이면 해당 원소의 인덱스 값은 해당 그룹에 포함되도록 했다.
하지만 이런 식의 방식은 dfs() 함수에서 오류가 발생했다.
반례는 아래와 같다.
(입력)
1
6 6
1 3
3 4
4 2
2 5
5 6
6 1
(출력): YES
'''

def dfs(n, graph, group_a, group_b):
    for i in range(1, n+1):
        if group_a[i]:                  # i가 group_a에 속해 있다면
            for j in graph[i]:  
                if group_a[j]:          # j가 group_a에 속해 있다면 
                    group_a[j] = False  # j를 group_a에서 제외하고
                    group_b[j] = True   # group_b에 추가한다.
    for i in range(1, n+1):
        if group_b[i]:                  # i가 group_b에 속해 있다면
            for j in graph[i]:
                if group_b[j]:          # i가 연결된 값이 group_b에 포함되면
                    return 'NO'         # 'No'를 반환하고 함수를 종료한다.
    return 'Yes'

for _ in range(int(input())):
    n, m = map(int, input().split())    # 노드와 간선을 입력받는다.
    graph = [[] for _ in range(n+1)]    # graph를 저장할 리스트를 생성한다.

    # 간선을 입력받는다.
    for _ in range(m):
        a, b = map(int, input().split())
        # 양방향 그래프이므로 두 노드 모두 저장해준다.
        graph[a].append(b)
        graph[b].append(a)

    # n이 1인 경우 성립하므로 Yes를 출력하고 다른 case를 조사하도록 continue를 써준다.
    if n == 1:
        print('Yes')
        continue

    '''
    group_a에는 모든 원소가 True 값을 가지고 group_b는 모든 원소가 False 값을 가지도록 한다.
    group_a에서 원소 하나씩 탐색하며 이어져 있는 원소들을 모두 빼내 group_b에 넣는다.
    그리고 group_b에 있는 원소 중에서 연결된 노드가 있다면 No를 출력하고
    연결된 노드가 없다면 Yes를 출력하게 한다.
    '''
    group_a = [True for _ in range(n+1)]
    group_b = [False for _ in range(n+1)]

    print(dfs(n, graph, group_a, group_b))



# My solution2(dfs, 1772ms)
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)          # recurstionlimit를 증가시키지 않으면 런타입 에러 발생
def dfs(now, n, visited, graph, group):
    visited[now] = True                 # 방문 한 곳은 방문처리 해준다.

    for i in graph[now]:
        if not visited[i]:
            group[i] = -group[now]      # 해당 노드(i)는 now와 다른 그룹에 속해야한다. 따라서 group[now]에 음수를 취한 값을 입력한다.
            dfs(i, n, visited, graph, group)

def find(n, graph, group):
    # dfs를 통해 각 노드에 그룹 번호를 매겼다.
    # 만약 인접 노드가 같은 값을 가진다면 이분 그래프가 아니다.
    for i in range(1, n+1):
        for j in graph[i]:
            if group[j] == group[i]:
                return "NO"
    return "YES"

for _ in range(int(input())):
    n, m = map(int, input().split())    # 노드와 간선을 입력받는다.
    graph = [[] for _ in range(n+1)]    # graph를 저장할 리스트를 생성한다.

    # 간선을 입력받는다.
    for _ in range(m):
        a, b = map(int, input().split())
        # 양방향 그래프이므로 두 노드 모두 저장해준다.
        graph[a].append(b)
        graph[b].append(a)

    visited = [False for _ in range(n+1)]
    group = [1 for _ in range(n+1)]     # 각 원소를 1 혹은 -1로 그룹을 매긴다. 같은 값을 가지면 같은 그룹이다.

    for i in range(1, n+1):
        if not visited[i]: # 아예 이어지지 않은 곳이 있을 수 있으므로 원소 하나를 방문하고 반복문을 통해 다른 노드의 방문 여부를 확인해야 한다.
            dfs(i, n, visited, graph, group)

    print(find(n, graph, group))


# My solution3(bfs, 1636ms)
# 위의 코드를 dfs방식에서 bfs방식으로 바꾼 것이다. 이외에 다른 것은 다 동일하다.
import sys
from collections import deque
input = sys.stdin.readline
def bfs(start, n, visited, graph, group):
    q = deque([start])
    visited[start] = True

    while q:
        now = q.popleft()
        for i in graph[now]:
            if not visited[i]:
                group[i] = -group[now]
                q.append(i)
                visited[i] = True

def find(n, graph, group):
    for i in range(1, n+1):
        for j in graph[i]:
            if group[j] == group[i]:
                return "NO"
    return "YES"

for _ in range(int(input())):
    n, m = map(int, input().split())    # 노드와 간선을 입력받는다.
    graph = [[] for _ in range(n+1)]    # graph를 저장할 리스트를 생성한다.

    # 간선을 입력받는다.
    for _ in range(m):
        a, b = map(int, input().split())
        # 양방향 그래프이므로 두 노드 모두 저장해준다.
        graph[a].append(b)
        graph[b].append(a)

    visited = [False for _ in range(n+1)]
    group = [1 for _ in range(n+1)]

    for i in range(1, n+1):
        if not visited[i]:
            bfs(i, n, visited, graph, group)

    print(find(n, graph, group))

# other solution(bfs, 1800ms)
import collections
import sys
input = sys.stdin.readline

for _ in range(int(input())):
    V, E = map(int, input().split())    # 노드, 간선 개수 입력
    graph = [[] for i in range(V+1)]    # 빈 그래프 생성
    visited = [0] * (V+1)               # 방문한 정점 체크

    for _ in range(E):
        a,b = map(int, input().split())
        graph[a].append(b) 
        graph[b].append(a)

    q = collections.deque()
    group = 1
    bipatite = True
    for i in range(1, V+1):
        if visited[i] == 0:                             # 방문하지 않은 정점이면 bfs 수행
            q.append(i)                                 # 방문할 곳을 queue에 넣어준다.
            visited[i] = group                          # 아직 방문한 적이 한번도 없으므로 1그룹에 넣는다.
            while q:                                    # 해당 노드의 그래프를 모두 탐색한다.
                v = q.popleft()                         # bfs 시작
                for w in graph[v]:                      # queue에서 꺼낸 노드와 인접한 노드를 하나 씩 확인한다.
                    if visited[w] == 0:                 # 방문하지 않은 정점이면 조건문을 실행한다.
                        q.append(w)                     # q에 삽입한다.
                        visited[w] = -1 * visited[v]    # 현재 노드와 다른 그룹으로 지정한다.
                    elif visited[v] == visited[w]:      # 이미 방문했다면 아래 조건문을 실행한다.
                        bipatite = False                # 이미 방문한 노드가 해당 노드와 그룹이 같다면 bipatite가 False 값을 가진다.

    print('YES' if bipatite else 'NO')

'''
다른 사람의 코드가 시간은 느리지만 배울만한 아이디어가 있다.
'이미 방문한 곳과 인접하다면 해당 노드와 현재 노드를 비교해본다'
는 아이디어를 사용하면 시간을 줄일 수 있을 것 같다.
현재 내코드는 모두 grouping을 하고 나중에 확인하기 때문에 확실히 좋은 아이디어다.
그리고 visited 리스트를 0으로 초기화 하고 그룹 번호를 입력해주는 것도 메모리적으로 더 좋은 것 같다.
아래는 수정해본 코드다.
'''

# My solution + Other solution (1672ms)
# 차이가 생각보다 별로 없다.
# 사실 내 find()함수는 많아봤자 노드의 개수 만큼만 반복된다.
# 즉, 최대 200,000밖에 반복되지 않아 시간상의 변화가 별로 없는 것 같다. 하지만 아래 방법도 꼭 알아두자.
import sys
from collections import deque
input = sys.stdin.readline
def bfs(start, n, visited, graph):
    q = deque([start])
    visited[start] = 1

    while q:
        now = q.popleft()
        for i in graph[now]:
            if visited[i] == 0:
                visited[i] = (-1) * visited[now]
                q.append(i)
            else:
                if visited[i] == visited[now]:
                    return True

for _ in range(int(input())):
    n, m = map(int, input().split())    # 노드와 간선을 입력받는다.
    graph = [[] for _ in range(n+1)]    # graph를 저장할 리스트를 생성한다.

    # 간선을 입력받는다.
    for _ in range(m):
        a, b = map(int, input().split())
        # 양방향 그래프이므로 두 노드 모두 저장해준다.
        graph[a].append(b)
        graph[b].append(a)

    visited = [0 for _ in range(n+1)]
    result = 'YES'
    for i in range(1, n+1):
        if visited[i] == 0:
            if bfs(i, n, visited, graph):
                result = 'NO'

    print(result)