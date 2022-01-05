# My Solution(640ms)
'''
어떤 양방향 그래프를 입력받고 숫자 데이터들을 입력받아
해당 숫자들이 BFS 탐색 결과인지 판단하는 프로그램이다.

처음엔 '모든 경우를 탐색해볼까?' 라고 생각했다.
하지만 노드가 100,000개 이고, 1에 나머지 99,999개의 노드가 연결되어 있다면,
O(100,000!)의 시간복잡도를 가진다. 따라서 시간내에 프로그램이 작동하지 못한다.

DP를 생각해봤지만, DP로 하기에는 어떠한 규칙을 점화식으로 표현할 수는 없다고 생각했다.
그래서 마지막으로 생각한 것이 입력받은 BFS 방문 순서를 활용해 탐색하는 방법이었다.

하는 법은 간단한다.
단순히 BFS를 수행하면서 해당 결과가 맞는지 확인하면서 가는 것이다.
하지만 이전 예시와 같은 경우에 단순 탐색으로 결과가 맞는지 확인하려면, O(100,000^2)이라는 시간복잡도를 가진다.
따라서 모든 노드의 graph리스트를 정렬해주고, 탐색은 이진 탐색을 활용해 총 nlogn이라는 시간으로 수행이 가능하다.
확인 방법은 아래 코드에서 확인하자.
'''

# 이진 탐색을 수행하는 함수다.
def binary_search(aim, arr):    
    left = 0
    right = len(arr)-1

    while left <= right:
        center = (left + right) // 2
        
        if arr[center] == aim:
            return True
        elif arr[center] < aim:
            left = center + 1
        else:
            right = center - 1

    return False

def bfs():
    '''
    BFS 방문 순서의 첫 번째 원소는 무조건 1이여야 한다.(문제에서 출발점은 1이라고 주어졌기 때문이다.)
    따라서 result의 첫번째 원소가 1인지 확인하고 아니라면 False를 반환하면서 함수를 종료한다.
    '''
    if result.popleft() != 1: return False          # 첫 번째 원소가 1인지 확인하고 아니라면 False를 반환한다.                  
    q = deque([1])                                  # 1을 원소로 가지고 있는 큐를 만든다.
    visited[1] = True                               # 1번째 노드에 방문 처리를 해준다.

    while q:
        now = q.popleft()                           # 첫 번째로 탐색할 원소를 찾는다.
        
        check = 0                                   # 해당 노드와 연결된 노드 중 아직 방문하지 않은 노드의 개수를 저장할 변수다. 
        for i in graph[now]:                        # 노드와 연결된 노드를 탐색한다.
            if not visited[i]:                      # 방문한 노드가 아니라면
                check += 1                          # check에 1을 더하고 방문 처리해준다.
                visited[i] = True                   
                
        for i in range(check):                      # 연결된 노드중 방문하지 않은 노드는 모두 탐색해야 한다. 따라서 check만큼 반복한다.
            next = result.popleft()                 # result의 처음 check개의 노드는 모두 graph[now]의 원소여야 한다. 따라서 첫 번째 원소부터 탐색해 큐에 넣어준다.
            if not binary_search(next, graph[now]): # binary_search를 사용해 해당 노드가 현재 노드와 연결되어 있는지 확인한다.
                return False                        # 연결되어 있지 않다면 틀린 탐색 결과이므로 False를 반환한다.
            q.append(next)                          # 연결되어 있다면 q에 해당 노드를 넣어준다.
            
    return True                                     # 모든 원소를 탐색했을 때 이상이 없으므로 True를 반환한다.

from collections import deque
import sys
input = sys.stdin.readline

n = int(input())                                    # 노드의 개수를 입력받는다.
graph = [[] for _ in range(n+1)]                    # 양방향 그래프를 저장할 리스트다.

for _ in range(n-1):                                # n-1개의 간선을 입력받는다.
    a, b = map(int, input().split())                # 연결된 두 노드를 입력받고 두 노드의 graph에 추가한다.
    graph[a].append(b)
    graph[b].append(a)

for i in range(len(graph)):                         # binary_search를 사용할 것이므로 graph의 각 원소를 미리 정렬해야 한다.
    graph[i].sort()

result = deque(map(int, input().split()))           # BFS 탐색 결과를 입력받는다.
visited = [False for _ in range(n+1)]               # 방문 여부를 저장할 리스트다.

if bfs(): print(1)                                  # 올바른 탐색 결과라면 1을 출력한다.
else: print(0)                                      # 올바르지 않다면 0을 출력한다.

# Other Solution1(496ms)
# 출처: https://vixxcode.tistory.com/28
'''
BFS 탐색 결과가 올바른지 확인하려면 주어진 순서를 기반으로 노드를 저장한 후 BFS 탐색을 수행해 같은 결과가 나오는 경우에만 가능한 경우로 판정하면 된다.

내 풀이를 돌아보자.
1. 큐에서 노드를 꺼낸다.
2. 노드와 연결된 노드중 이전에 방문하지 않았던 노드의 개수를 센다.
3. 노드의 개수만큼 result의 원소를 빼주면서 해당 노드가 graph[now]에 있는지 확인한다. (이진 탐색이므로 탐색에서 O(logn)의 시간 복잡도를 가진다.)
   - 해당 노드들이 모두 graph[now]에 들어있는 노드라면 순서대로 q에 저장하고 bfs를 계속 수행한다.
   - 해당 노드 중 graph[now]에 있지 않은 노드가 있다면 함수를 종료한다.

아래 코드는 다음과 같이 진행된다.
1. 큐에서 노드를 꺼낸다.
2. 노드와 연결된 노드중 이전에 방문하지 않았던 노드들을 리스트(stk)에 저장한다.
3. 해당 노드의 길이 만큼 result의 원소를 복사해 리스트(li)에 저장한다. 해당 리스트와 동일한 리스트(tmp)도 만들어 준다.
4. 리스트(li)를 정렬한다. result의 원소들은 무작위로 나열되어 있으므로 확인하려면 두 가지 방식으로 확인할 수 있다.
   (1) 내 방식처럼 하나의 원소씩 비교해본다.
   (2) 두 리스트를 정렬해 두 리스트가 같은지 확인한다.
   아래 코드는 2번의 방식을 사용했다.
5. result의 원소를 복사한 리스트(li)와 방문하지 않은 연결된 노드를 저장한 리스트(stk)와 동일하지 않다면 flag에 True를 지정하고 함수를 종료한다.
   두 리스트가 동일하다면 result에서의 순서대로 저장된 리스트(tmp)의 원소들을 하나씩 큐에 넣어준다.
'''
import sys
from collections import deque

N = int(sys.stdin.readline().rstrip())                  # 노드의 개수를 입력받는다.
graph=[[] for _ in range(N+1)]                          # 양방향 그래프를 저장할 리스트를 생성한다.
for _ in range(N-1):                                    # n-1개의 간선을 입력받아 그래프를 그린다.
    a,b= map(int,sys.stdin.readline().rstrip().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1,N+1):                                  # graph의 모든 원소(리스트)를 정렬한다.
    graph[i].sort()
ans=list(map(int,sys.stdin.readline().split()))         # BFS 탐색 결과를 입력받는다.
                                                 
flag=False                                              # 탐색 결과가 올바른지 틀린지 확인해줄 변수다.
visited = [False]*(N+1)                                 # 방문 여부를 저장할 리스트다.
def bfs(n):
    global flag                                         # flag를 global 변수로 지정한다.
    q =deque()                                          # 큐를 생성한다.
    q.append(n)                                         # q에 첫 번째 원소를 넣어주고 방문 처리해준다.
    visited[n]=True                                     
    
    start=1                                             # 0번째 원소는 무조건 1이므로 ans의 첫 번째 원소부터 탐색하기 위해 1로 초기화한다.
    tmp=[]
    while q:
        stk=[]
        for i in graph[q.popleft()]:                    # 큐의 첫 번째 원소를 꺼내 연결된 노드를 확인한다.
            if not visited[i]:                          # 해당 노드를 방문한 적이 없다면
                stk.append(i)                           # stk에 i를 추가하고 방문 처리해준다.
                visited[i]=True                        
                
        li=ans[start:start+len(stk)]                    # start~start+len(stk)-1 인덱스의 원소를 li에 저장한다.
        tmp=list(li)                                    # li와 동일한 리스트를 한 개 생성한다.
        start=start+len(stk)                            # start에 미리 len(stk)를 더해 다음에 탐색을 시작할 인덱스를 저장한다.
        li.sort()                                       # graph의 모든 원소를 sort했기 때문에 li를 sort에 동일한지 확인해야 한다.
        if li!=stk:                                     # li가 stk와 같지 않다면 BFS 탐색 결과가 틀린 것이다.
            flag=True                                   # flag를 True로 지정하고 함수를 종료한다.
            break
        else:                                           # 현재까지 올바른 탐색 결과이다.
            for i in tmp:                               # tmp의 원소들을 하나씩 꺼내면 큐에 저장하면 주어진 BFS 탐색 결과와 동일하게 탐색할 수 있다.
                q.append(i)                             

if ans[0]==1:                                           # ans[0]은 무조건 1이여야 하므로 확인해준다.
    bfs(1)                                              # bfs를 수행한다.
    print(1) if not flag else print(0)                  # flag가 False라면 올바른 결과이므로 1을 출력하고 아니라면 0을 출력한다.
else:                                                   # ans[0]이 1이 아니라면 0을 출력해야 한다.
    print(0)

# Other Solution2(388ms)
'''
기본적인 알고리즘은 Other Solution1과 같다.
'''
import sys
input = sys.stdin.readline
def sol():
    N = int(input())                                    # 노드의 개수를 입력받는다.                         
    edges = [[] for _ in range(N + 1)]                  # 양방향 그래프를 저장할 리스트를 생성한다.
    for i in range(N - 1):                              # n-1개의 간선을 입력받는다.
        s, e = map(int, input().split())
        edges[s].append(e)
        edges[e].append(s)
    arr = tuple(map(int, input().split()))              # BFS 탐색 결과를 입력받는다.
    
    visited = [True] * (N + 1)                          # 방문 여부를 저장할 리스트다.
    visited[1] = False                                  # 1은 미리 방문처리를 해준다.
    idx = 1                                             # arr의 0번째 원소를 확인할 필요는 없으니 1을 저장한다.
    for i in arr:                                       # arr의 모든 노드를 순서대로 탐색한다.
        if visited[i]:                                  # 해당 노드를 방문한적이 없다면
            return 0                                    # 0을 반환해 함수를 종료한다.

        next_list = []                                  # 다음에 이동할 수 있는 노드를 저장할 리스트다.
        for e in edges[i]:                              # 현재 노드와 연결된 노드를 확인한다.
            if visited[e]:                              # 해당 노드를 방문한적이 없다면
                visited[e] = False                      # 방문처리를 해주고 next_list에 추가한다.
                next_list.append(e)
        next_list.sort()                                # next_list를 sort한다.

        new_arr = sorted(arr[idx:idx + len(next_list)]) # arr의 idx~idx+len(next_list)-1 원소들을 정렬한 리스트이다.
        '''
        모든 원소를 하나씩 비교하는 방법과 두 리스트를 한 번에 비교하는 방법
        두 가지 방식을 사용해봤다.
        두 번째 방식이 더 빠른 효과를 보여줬다.(360ms)
        '''
        for i in range(len(next_list)):                 # next_list의 원소들과 new_arr의 원소들을 비교하기 위해 next_list의 길이 만큼 반복한다.
            if new_arr[i] != next_list[i]:              # 두 리스트는 모두 정렬되어 있으므로 동일한 인덱스의 원소는 같아야 한다.
                return 0                                # 따라서 같지 않은 경우에는 0을 반환하고 함수를 종료한다.

        if new_arr != next_list: return 0               # 두 리스트가 같지 않으면 0을 반환한다.
        idx += len(next_list)                           # idx는 len(next_list)를 더해 다음에 탐색할 인덱스로 갱신한다.
                                 
    return 1                                            # 모든 결과가 올바르므로 1을 반환한다.
print(sol())