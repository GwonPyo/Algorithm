# My Solution1(dfs, 68ms) 

'''
dfs를 이용해 풀었다. 문제 자체는 dp스러운데 dfs를 이용해서 풀 수 있을 것 같았다.
먼저 핵심 아이디어는 이전에 탐색했던 노드(날짜)는 해당 날짜를 탐색할 때 탐색하지 않아도 된다는 것이다.
예를 들어, 1일차부터 상담을 시작할 때 4일 차의 상담을 수행할 수 있어 해당 날짜를 탐색했다고 가정하자.
그러면 4일차의 상담부터 시작하여 탐색할 필요가 없다. 
4일차 상담으로 가능한 모든 경우에는 1일차의 이익을 추가했기 때문에 최대 이득이 될 수 없기 때문이다.
단, 1일차에 4일차 상담을 탐색했어도 2일차에는 4일차의 상담을 탐색해야 한다.
'''

import sys
input = sys.stdin.readline
n = int(input())                            # 1 ≤ N ≤ 15
data = [0 for _ in range(n)]                # 상담의 정보를 담을 리스트
for i in range(n):                          # 각 날짜 별로 상담 시간과 이익을 입력받는다.
    time, cost = map(int, input().split())
    if i+time <= n: data[i] = (time, cost)  # 해당 날짜에 상담을 시작했을 때 상담 기간이 퇴사 예정 날을 넘긴다면 data[i]의 값을 갱신하지 않는다.

result = 0                                  # 최대값을 담을 변수다.
def dfs(now, profit):                       # 현재 일자와 지금까지의 수익을 인자로 받는다.
    global result   
    
    if data[now] == 0:                      # 해당 날짜에 상담을 시작했을 때 상담 기간이 퇴사 예정 날을 넘기면
        result = max(result, profit)        # 더 이상 탐색할 수 없으므로 result를 갱신한다.
        return
    
    time, cost = data[now]                  # 상담 정보를 time, cost변수에 저장한다.
    if now+time == n:                       # 현재 날짜와 상담 기간(time)을 더했을 때 퇴사 예정일이 되면
        result = max(result, profit+cost)   # result를 갱신한다.
        return

    for i in range(now+time, n):            # 이후 상담 날짜로 삼을 수 있는 모든 날짜를 탐색한다.
        check[i] = True                     # check[i]를 갱신한다.
        dfs(i, profit+cost)                 # dfs를 수행한다.

check = [False for _ in range(n)]           # 위에 설명한 핵심 아이디어를 위한 리스트다.
for i in range(n):                          # 모든 날짜를 탐색한다.
    if not check[i]:                        # 해당 날짜를 탐색한 적이 없다면
        check[i] = True                     # check를 갱신한다.
        dfs(i, 0)                           # 그리고 해당 날짜를 상담 시작일로 삼고 dfs를 수행한다.

print(result)

# My Solution2(dp, 68ms)

'''
문제가 dp스러워서 dp로도 풀어봤다.
'''

import sys
input = sys.stdin.readline

n = int(input())                                    # 1 ≤ N ≤ 15
data = []                                           # 상담의 정보를 담을 리스트
for i in range(n):
    time, cost = map(int, input().split())
    data.append((time, cost))                       # 각 날짜 별로 상담 시간과 이익을 입력받는다.

dp = [0 for _ in range(n+1)]                        # 메모이제이션에 사용할 리스트다.

for i in range(n-1, -1, -1):                        # n-1~0일차까지 탐색한다.
    time, cost = data[i]                            # 상담 정보를 time, cost변수에 저장한다.
    if i+time > n: dp[i] = dp[i+1]                  # 만약 해당 상담을 진행할 때 퇴사 기간을 넘긴다면, 이전에 탐색한 i+1의 최대값을 저장한다.
    else: dp[i] = max(dp[i+1], cost + dp[i+time])   # 상담 이후 퇴사날이 되지 않으면, i+time의 최대값과 cost를 더한 값과 i+1의 최대값을 비교한다.

print(dp[0])