import sys
from collections import deque
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n, k = map(int, input().split()) # 건물수, 건물간의 규칙
    building = [0] + list(map(int, input().split())) # 각 건물의 건설 시간
    tree = [[] for _ in range(n + 1)] # 건설 순서 규칙 (내 코드에서 graph의 역할과 동일)
    inDegree = [0 for _ in range(n + 1)] # 진입 차수 (해당 건축물을 짓기 한 번전에 지어야하는 건축물의 수)
    dp = [0 for _ in range(n + 1)] # 해당 건물까지 걸리는 시간

    for _ in range(k):
        a, b = map(int, input().split())
        tree[a].append(b)
        inDegree[b] += 1
    
    q = deque()
    for i in range(n + 1):
        if inDegree[i] == 0:
            # 1. 출발점으로 할 수 있는 건물을 찾는다.
            # 2. 큐에 넣어준다.
            q.append(i)
            dp[i] = building[i]
    # 이로써 q에는 건설 가능한 친구들만 남는다.
    while q:
        a = q.popleft()
        for i in tree[a]:
            # 1. a(현재 건물)다음에 이어진 건물의 진입 차수를 줄인다.
            inDegree[i] -= 1
            # 2. a다음에 이어진 건물의 걸리는 시간(dp[i])를 갱신한다.
            # dp[i]: 지금까지 확인한 건설 시간
            # dp[a] + building[i]: dp[i]랑 비교할 건설 시간
            dp[i] = max(dp[a] + building[i], dp[i])
            # 3. 이로써 i이전의 건축물이 더이상 없다면, 큐에 i를 추가해준다.
            if inDegree[i] == 0:
                q.append(i)
    
    answer = int(input())
    print(dp[answer])