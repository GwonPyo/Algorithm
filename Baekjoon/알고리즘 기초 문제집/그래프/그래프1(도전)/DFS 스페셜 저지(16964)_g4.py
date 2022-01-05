# My Solution1(620ms)
'''
입력된 dfs 탐색 결과의 순서대로 탐색하는 방식을 사용했다.
자세한 설명은 아래 코드를 참고하자.
'''
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

n = int(input())                                        # 노드의 개수를 입력받는다.
graph = [[] for _ in range(n+1)]                        # 양방향 그래프를 저장할 리스트다.

for _ in range(n-1):                                    # n-1개의 간선에 대한 정보를 입력받는다.
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1, n+1):                                 # graph의 모든 원소를 정렬한다.(이진 탐색을 사용하기 위해서다. 이진 탐색을 사용하는 이유는 아래에서 살펴보자.)
    graph[i].sort()

result = list(map(int, input().split()))                # dfs 탐색 결과를 입력받는다.
visited = [False for _ in range(n+1)]                   # 각 노드의 방문 여부를 확인해줄 리스트다.

# 이진 탐색을 수행해주는 함수다. 원소가 있다면 True 없다면 False를 반환한다.
def binary_search(aim, arr):                            
    l = 0; r = len(arr)-1

    while l <= r:
        center = (l+r)//2
        if arr[center] == aim:
            return True
        elif arr[center] < aim:
            l = center+1
        else: r = center-1

    return False

def dfs(now):
    global index                                        # index를 global변수로 지정한다.
    index += 1                                          # index를 갱신해준다.

    next_node = []                                      # 다음에 이동할 수 있는 노드들을 저장할 리스트다.
    for i in graph[now]:                                # 현재 노드와 연결된 모든 노드를 탐색한다.
        if not visited[i]:                              # 해당 노드를 방문한 적이 없다면
            next_node.append(i)                         # next_node에 저장하고 방문처리한다.
            visited[i] = True

    '''
    이진 탐색이 아니라 그냥 탐색을 사용한다면 무조건 시간 초과가 발생할 것이다.
    따라서 이전해 정렬을 해놓고 이진 탐색을 사용해서 비용을 줄였다.
    '''
    for _ in range(len(next_node)):                     # next_node의 원소 개수만큼 dfs를 수행해야한다.
        if binary_search(result[index], next_node):     # 만약 result[index]가 next_node에 포함되었다면
            if not dfs(result[index]): return False     # dfs를 수행하고, dfs의 결과가 False라면 False를 반환한다.
        else: return False                              # result[index]가 next_node에 포함되지 않았다면 False를 반환한다.

    return True                                         # next_node에 들어있는 노드를 모두 방문했고 결과가 올바르다는 의미이므로 True를 반환한다.

index = 0                                               # 확인해야할 result 원소의 인덱스 번호이다.
visited[1] = True                                       # 노드 1에서 출발하는 것이 문제에서 주어졌으므로 1을 방문처리한다.
if result[index] == 1:                                  # 0번째 원소가 1이라면
    print(1 if dfs(1) else 0)                           # dfs를 수행해 True를 반환하면 1, False를 반환하면 0을 출력한다.
else: print(0)                                          # 0번째 원소가 1이 아니라면 0을 출력한다.

# My Solution2(384ms)
'''
부모 노드가 올바른지 확인하는 방식을 사용했다.
자세한 설명은 아래 코드를 참고하자.
'''
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

n = int(input())                                        # 노드의 개수를 입력받는다.
graph = [[] for _ in range(n+1)]                        # 양방향 그래프를 저장할 리스트다.

for _ in range(n-1):                                    # n-1개의 간선에 대한 정보를 입력받는다.
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

result = list(map(int, input().split()))                # dfs 탐색 결과를 입력받는다.
visited = [False for _ in range(n+1)]                   # 각 노드의 부모 노드를 저장해줄 리스트다.
def dfs(now):
    global index                                        # index를 global 변수로 지정한다.
    index += 1                                          # index값을 갱신한다.

    next_node = []                                      # 다음에 이동할 수 있는 노드들을 저장할 리스트다.
    for i in graph[now]:                                # 현재 노드와 연결된 모든 노드를 탐색한다.
        if not visited[i]:                              # 해당 노드를 방문한 적이 없다면
            next_node.append(i)                         # next_node에 저장하고 visited값을 현재 노드로 지정한다. (즉, 현재 노드를 부모 노드로 지정한다.).
            visited[i] = now                            
    for i in range(len(next_node)):                     # next_node의 원소 개수만큼 dfs를 수행해야한다.
        if visited[result[index]] != now: return False  # 만약 result[index](result의 index번째 원소)가 현재 노드가 아니라면, 잘못된 탐색 결과인 것이다. 따라서 False를 반환한다.
        if not dfs(result[index]): return False         # dfs를 수행한 결과가 False라면 False를 반환한다.
        
    return True                                         # 지금까지 모든 dfs 탐색 결과가 올바르다는 의미이므로 True를 반환한다.

index = 0                                               # 확인해야할 result 원소의 인덱스 번호이다.
visited[1] = True                                       # 노드 1에서 출발하는 것이 문제에서 주어졌으므로 1을 방문처리한다.
if result[index] == 1:                                  # 0번째 원소가 1이라면
    print(1 if dfs(1) else 0)                           # dfs를 수행해 True를 반환하면 1, False를 반환하면 0을 출력한다.
else: print(0)                                          # 0번째 원소가 1이 아니라면 0을 출력한다.

# Other Solution(268ms)
'''
솔직히 왜 아래 코드가 가장 빠른지는 잘 모르겠다.
내 처음 코드와 다른점은 graph를 정렬하지 않고, binary_search를 사용하지 않는다는 점이다.
즉, 내 코드는 binary_search를 사용하고 아래 코드는 단순 탐색을 사용한다.

처음에 binary_search를 사용해 풀었던 이유는 노드의 수가 2이상 100,000이하이기 때문이다.
만약 노드 1에 99,999개의 노드가 연결되어 있다면, 이를 확인하는데 O(n^2)의 시간이 소요된다.
그런데 아래 코드는 아주 빠르다.

그래도 얻어간 것이 하나있다.
이전에 탐색을 빠르게 하기 위해사 부모 노드를 이용해 O(1)의 시간을 소요해 탐색을 수행할 수 있었다.
하지만 set을 이용해도 마찬가지로 O(1)을 소요해 탐색할 수 있다.
따라서 다음에 탐색이 필요할 때 list가 아니라 set을 이용할 수 있다면 set을 이용하는 것이 좋겠다. 
'''
import sys
from collections import deque
input = sys.stdin.readline

def dfs():
    n = int(input())                                        # 노드의 개수를 입력받는다.
    graph = [[] for _ in range(n+1)]                        # 양방향 그래프를 저장할 리스트다.

    for _ in range(n-1):                                    # n-1개의 간선에 대한 정보를 입력받는다.
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    result = deque(list(map(int, input().split())))         # dfs 탐색 결과를 입력받는다.
    visited = [True] + [False for _ in range(n)]            # 방문 여부를 확인해줄 리스트다.

    stack = []                                              # stack을 생성하고 출발점인 1을 추가한다.
    stack.append(1)                                         

    if result.popleft() != 1:                               # 첫 번째 원소가 1이 아니라면 0을 출력하고 함수를 종료한다.
        print(0)
        return
    visited[1] = True                                       # 1을 방문처리한다.

    while len(stack) > 0:                                   # stack의 길이가 0이 아닐 때까지 반복한다.
        now = stack.pop()                                   # stack의 원소 하나를 꺼낸다.
        next_node = []                                      # 다음에 이동할 수 있는 노드들을 저장할 리스트다.                            
        for i in graph[now]:                                # 현재 노드와 연결된 모든 노드를 탐색한다.
            if not visited[i]:                              # 해당 노드를 방문한 적이 없다면
                next_node.append(i)                         # next_node에 추가한다.       
        '''
        'in'의 시간복잡도
        1. list, tuple: O(n)
        2. set, dict: O(1) [해시에서 충돌이 많은 경우 O(n)]
        '''
        for _ in range(len(next_node)):                     # next_node의 원소 개수만큼 dfs를 수행해야한다.
            next = result.popleft()                         # dfs 탐색 결과에서 확인해야할 원소를 꺼낸다.
            if next in next_node:                           # 해당 원소가 next_node에 포함된다면(현재 노드와 연결되어 있다면)
                stack.append(next)                          # stack에 next를 추가하고 방문처리한다.
                visited[next] = True                        
                break
            else:                                           # 그렇지 않다면 0을 출력하고 함수를 종료한다.
                print(0)
                return
    print(1)                                                # dfs 탐색 결과가 올바르다는 의미이므로 1을 출력한다.

dfs()