# My Solution(236ms)
'''
스타트와 링크(14889)_s3.py[브루트 포스(비트마스크)]의 심화 문제다. 
아래 코드가 이해되지 않는다면 위 문제의 코드를 참고하자.

처음에는 얼마나 많은 사람을 시작점으로 두고 반복해야 하는지 고민했다.
하지만 생각해보면 0번째 사람부터 사전순으로 모든 경우를 탐색하면
아래 조건문을 사용하여 여러 사람을 시작점으로 두고 반복하는 것보다 빠르게 수행이 가능하다.
if prev_result < 0 and abs(prev_result) >= result: return
예를 들어, 총 인원이 6명일 때 (0, 1, 2)만 탐색했는데 해당 조건을 만족한다고 하자.
그러면 이후에 (4, 5, 6), (4, 5), (4, 6), (5, 6), (4), (5), (6)은 탐색하지 않는다.

해당 방법이 성립하는지 의구심이 든다면, 4명의 인원이 있다고 가정하고 첫 번째 사람을 기준으로만 직접 탐색해보자.
모든 경우를 탐색할 수 있다.
'''

import sys
input = sys.stdin.readline

n = int(input())                                                # 인원수를 입력받는다.(4 ≤ N ≤ 20)
graph = [list(map(int, input().split())) for _ in range(n)]     # 인원들의 관계를 입력받는다.  

row_col_sum = []                                                # 각 인원마다 해당 인원이 속했을 때 얻는 점수를 총합한 값을 row_col_sum에 저장한다.
for r, c in zip(graph, zip(*graph)):                            # 예를들어 0번째 사람은 0번째 열과 0번째 행을 더하면 된다.
    row_col_sum.append(sum(r)+sum(c))

all_sum = sum(row_col_sum) // 2                                 # 총 점수를 구한다. row_col_sum의 값을 모두 더하면 모든 점수가 두 번씩 더해지므로 2의 몫으로 지정해야 한다.

result = float("inf")                                           # 결과를 저장할 변수다.
def dfs(now, prev_result, count):                               # now: 현재 탐색하고 있는 인원(ex) 0번째 인원을 탐색한다면 0) / prev_result: 지금까지의 차이값 / count: 체크한 인원 수 
    global result                                               # result를 global로 지정한다.
    result = min(result, abs(prev_result))                      # prev_result와 result중 더 작은 값을 prev_result에 저장한다.
    
    if prev_result < 0 and abs(prev_result) >= result: return   # prev_result에 이후 탐색하는 위치의 row_col_sum을 빼줘야하므로 절대값이 result 이상이면 탐색을 종료해도 된다.
    if count == n-1: return                                     # 팀에는 최소 1명 이상이 있어야 한다. 따라서 n-1개를 탐색했다면 탐색을 종료한다.

    for i in range(now+1, n):                                   # 1~n-1을 사전순으로 탐색하면서 dfs를 수행한다.
        dfs(i, prev_result-row_col_sum[i], count+1)             

dfs(0, all_sum-row_col_sum[0], 1)                               # 0번째만 탐색해주면 모든 조합을 탐색한 효과를 얻을 수 있다.
print(result)