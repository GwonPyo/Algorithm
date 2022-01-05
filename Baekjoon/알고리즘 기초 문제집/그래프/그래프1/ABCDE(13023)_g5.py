# My Solution (2021.11.12)

'''
문제 조건은 아래와 같다.
1. a는 b와 친구다.
2. b는 c와 친구다.
3. c는 d와 친구다.
4. d는 e와 친구다.
위 조건을 만족하는 친구 관계가 존재하는지 확인하는 것이 문제의 목적이다.

처음에는 문제의 의미를 잘 이해하지 못했다.
잘 읽어보면 트리처럼 한줄로 쭉 이을 수 있는 5개의 노드가 있냐는 의미이다.
a - b - c - d - e 

문제를 풀기 위해 그래프 탐색인 dfs, bfs중 하나를 선택했다.
visited가 매번 달라지기 때문에 bfs에 visited를 계속 넣어주기에는 코드가 복잡해질 것 같았다.
그래서 visited를 조정하기 좀 더 편한 dfs를 사용하기로 했다.
'''

import sys
input = sys.stdin.readline
# 5 <= n <= 2000, 1 <= m <= 2000
n, m = map(int, input().split())

graph = [[] for _ in range(n)]
visited = [False for _ in range(n)]

# 그래프 생성(친구 관계는 양방향이므로 양방향 그래프를 그려줬다.)
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# 처음에 제출한 dfs 코드이다.
def dfs(now, count):
    visited[now] = True
    '''
    count는 현재까지 방문한 노드 수(친구 수)이다.
    아래에서 다음에 이동할 수 있는 노드(친구)가 있다면 해당 친구까지 포함한 인원을 체크한다.
    현재까지의 인원이 count였으므로 count에 미리 1을 더해준다.
    '''
    count += 1

    for next in graph[now]:
        if not visited[next]:
            visited[next] = True
            # 이동할 수 있는 노드가 있으므로 count가 5인지 체크한다.
            if count == 5:
                return True
            # 아직 친구수가 5가 아니라면 해당 노드로 이동해 dfs를 다시 수행한다.
            if dfs(next, count):
                return True
            # dfs를 수행해도 친구 수가 5인 경우가 없다면 해당 노드(next)의 방문 여부를 False로 바꾼다.
            # 다른 dfs를 사용했을 때 해당 노드를 방문할 수 없다면 제대로 된 확인이 불가능하다.
            visited[next] = False
  
    # dfs를 모두 수행해도 5인 경우를 찾지 못한 경우 False를 반환한다. 
    return False

# 조금 더 직관적으로 짠 dfs 코드이다.
def dfs2(now, count):
    visited[now] = True
  
    #지금까지 확인한 노드 수가 5인지 확인하는 조건문을 앞에 써줬다.
    if count == 5:
        return True

    for next in graph[now]:
        if not visited[next]:
            visited[next] = True
            # 이전에 count에 1을 더해 dfs를 수행해본다.
            if dfs(next, count+1):
                return True
            # 이전 dfs와 동일한 이유로 방문 여부를 False로 지정한다..
            visited[next] = False
    return False
    

def check():
    # 모든 노드에서 dfs를 진행한다.
    for now in range(n): 
        # 만약 dfs() 함수에서 친구 수가 5인 경우를 찾았다면 함수를 종료한다.
        if dfs(now, 1): return 1
        # dfs() 함수와 동일한 이유로 방문 여부를 False로 지정한다.
        visited[now] = False 
    return 0

print(check())

# other solution
import sys
input = sys.stdin.readline
def main():
    n, m = map(int, input().split())
    # 내 코드에서 graph와 동일하다(path)
    path = [[] for i in range(n)]

    # graph를 그려준다.
    for i in range(m):
        a, b = map(int, input().split())
        path[a].append(b)
        path[b].append(a)
    
    # 0 ~ n 까지 친구를 한 명 고른다.
    for a in range(n):
        # a와 연결된 노드(친구)중 하나를 선택한다.
        # a와 b가 동일할 일은 없으므로 조건문은 필요없다.
        for b in path[a]:
            # b에서 연결된 노드(친구)중 하나를 선택한다. 
            for c in path[b]:
                # b에는 a가 연결되어 있다.
                # 따라서 a로 이동하지 않도록 아래 조건문을 써준다.
                if c == a:
                    continue
                # c와 연결된 노드중 a와 b가 아닌 것을 고른다.
                for d in path[c]:
                    if d == a or d == b:
                        continue
                    # d와 연결된 노드중 a, b, c가 아닌 것을 고른다.
                    for e in path[d]:
                        if e != a and e != b and e != c:
                            # a, b, c가 아니라면 조건에 만족하므로 1을 반환한다.
                            return 1
    # 모든 반복문을 끝 마쳐도 찾지 못 했으므로 0을 반환한다.
    return 0
print(main())