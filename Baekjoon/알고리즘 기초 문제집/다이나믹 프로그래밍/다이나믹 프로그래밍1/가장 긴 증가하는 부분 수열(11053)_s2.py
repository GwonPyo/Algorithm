# My Solution(dfs+dp, 240ms)
'''
풀이법이 잘 생각나지 않아서 오래 고민했다.
아래 코드는 dp와 dfs를 이용해 사용한 풀이이다.
아래는 dfs에 응용할 핵심 개념들을 설명한 것이다.
1. 탐색을 시작할 위치는 '이전에 한 번도 탐색하지 않은 인덱스'를 기준으로 시작한다.
1번째 인덱스에서 시작하는 것 보다, 2번째 인덱스에서 시작하는 것의 결과가 더 클 수도 있다.
하지만 1번째 인덱스에서 시작해 탐색한 적이 있는 인덱스를 기준으로 시작한다면, 무조건 이전 탐색보다 값이 작을 수 밖에 없으므로 수행할 필요가 없다.
2. 위 처럼 1번째 인덱스와 2번째 인덱스 각각을 시작점으로 두고 탐색했을 때 결과가 다를 수 있다.
하지만 이때 3번째 인덱스를 같이 탐색할 것이다. 이렇게 동일한 연산이 반복되므로 dp를 생성했다. 
단, dp값이 0이 될 수도 있으므로 dp 원소들의 초기값은 -1로 설정했다.
3. n번째 인덱스를 기준으로 이후에 더 큰 값이 없을 수도 있다. 이를 위해 처음에 dp[now]를 0으로 갱신해야 한다. 
'''
n = int(input())                                    # 1 ≤ N(수열의 크기) ≤ 1,000
datas = list(map(int, input().split()))             # 수열의 원소를 담은 리스트다.
dp = [-1 for _ in range(n)]                         # dynamic programming에 활용할 dp리스트다. (dfs의 visited 리스트의 역할을 동시에 한다.)
graph = [[] for _ in range(n)]                      # dfs에 활용할 graph이다.

for i in range(n):                                  # graph 원소들을 갱신한다.(각 인덱스에서 다음에 올 수 있는 인덱스를 찾아 저장한다.)
    for j in range(i+1, n):
        if datas[i] < datas[j]:
            graph[i].append(j)

def dfs(now):                                
    dp[now] = 0                                     # 다음 인덱스에 더 큰 값이 없을 수도 있으므로 미리 값을 0으로 갱신한다. (= 방문처리한다.)
    for i in graph[now]:                            # 다음 인덱스에 더 큰 값이 있다면
        if dp[i] == -1:                             # 해당 인덱스를 이전에 탐색한 적이 없다면
            dp[now] = max(dp[now], dfs(i)+1)        # 탐색 후 현재 dp[now]의 값을 갱신한다. 
        else:                                       # 해당 인덱스를 이전에 탐색한 적이 있다면
            dp[now] = max(dp[now], dp[i]+1)         # 바로 dp[now]의 값을 갱신한다.
    return dp[now]                                  # 갱신한 dp[now]의 값을 반환한다.

result = 0
for i in range(n):
    if dp[i] == -1:
        dfs(i)

print(max(dp)+1)                                    # 모든 dp원소들은 자신의 값을 포함하지 않은 값이므로 1을 더하고 출력한다.

# Other Solution(dp, 156ms)
'''
아래 문제는 dp를 활용한 풀이다.
dp의 임의의 n번째 인덱스의 원소는 0~n-1번째 인덱스의 원소 중 가장 큰 값을 찾아 저장한다.
단, 해당 인덱스의 수열값은 n번째 인덱스의 수열값보다 작아야한다.
'''
n = int(input())                                    # 1 ≤ N(수열의 크기) ≤ 1,000
datas = list(map(int, input().split()))             # 수열의 원소를 담은 리스트다.
dp = [0 for _ in range(n)]                          # 이전 원소 중 가장 큰 값을 저장한 리스트다.
for i in range(n):                                  # 0~n-1까지 모든 인덱스를 탐색한다.
    for j in range(i):                              # 0~i-1까지 i이전의 모든 데이터를 탐색한다.
        if datas[i] > datas[j] and dp[i] < dp[j]:   # i보다 수열값은 작고, dp값은 가장 큰 원소를 찾고 해당 원소값으로 dp를 갱신한다.
            dp[i] = dp[j]
    dp[i] += 1                                      # dp값은 이전 원소값의 값이기 때문에 1을 더해준다.
print(max(dp))                                      # dp값중 가장 큰 값을 반환한다.