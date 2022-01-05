# My Solution(dfs, 72ms)
'''
수열의 조건은 다음과 같다.
1. N개의 자연수 중에서 M개를 고른 수열 (단, N개의 자연수는 모두 다른 수이다.)
2. 같은 수를 여러 번 골라도 된다.
3. 고른 수열은 비내림차순이어야 한다.
(길이가 K인 수열 A가 A1 ≤ A2 ≤ ... ≤ AK-1 ≤ AK를 만족하면, 비내림차순이라고 한다.)

비내림차순이므로 이전에 뽑은 인덱스~n까지 탐색해주면 된다. 
'''
import sys
input = sys.stdin.readline

n, m = map(int, input().split())        # n: 총 숫자의 개수, m: 결과를 구성할 숫자의 개수
data = list(map(int, input().split()))  # data를 입력받는다.
data.sort()                             # 사전순으로 출력하기 위해 정렬한다.
data = list(map(str, data))             # 출력에서 시간을 줄이기 위해 str로 변형한다.

result = []                             # 결과를 저장할 리스트다.
def dfs(now, count):        
    if count == m:                      # m개의 숫자를 뽑았다면 
        print(' '.join(result))         # 결과를 출력하고 함수를 종료한다.
        return

    for i in range(now, n):             # 비내림차순이므로 이전에 뽑았던 now~n까지를 탐색하면 된다. (오름차순은 now+1~n을 탐색하면 된다.)
        result.append(data[i])          # result에 해당 인덱스의 데이터를 넣어준다.
        dfs(i, count+1)                 # dfs를 수행한다.
        result.pop()                    # 해당 인덱스를 뽑는 경우는 모두 탐색했으므로 result에서 빼준다.

dfs(0, 0)
        
# Other Solution(combinations_with_replacement, 68ms)
'''
itertools에 combinations_with_replacement를 사용하면 중복 조합을 뽑을 수 있다.
사용법은 combinations와 동일하다.
'''
from itertools import combinations_with_replacement
import sys
input = sys.stdin.readline

n, m = map(int, input().split())        # n: 총 숫자의 개수, m: 결과를 구성할 숫자의 개수
data = list(map(int, input().split()))  # data를 입력받는다.
data.sort()                             # 사전순으로 출력하기 위해 정렬한다.
data = list(map(str, data))             # 출력에서 시간을 줄이기 위해 str로 변형한다.
print('\n'.join(map(' '.join, combinations_with_replacement(data, m))))
