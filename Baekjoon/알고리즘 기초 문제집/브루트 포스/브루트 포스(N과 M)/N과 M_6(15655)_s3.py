# My Solution1(combinations, 72ms)
'''
수열의 조건은 다음과 같다.
1. N개의 자연수 중에서 M개를 고른 수열 (단, N개의 자연수는 모두 다른 수이다.)
2. 고른 수열은 오름차순이어야 한다.

오름차순이므로 combination을 이용해 뽑아주면 된다.
'''
from itertools import combinations
import sys
input = sys.stdin.readline

n, m = map(int, input().split())        # n: 총 숫자의 개수, m: 결과를 구성할 숫자의 개수
data = list(map(int, input().split()))  # data를 입력받는다.
data.sort()                             # 사전순으로 출력하기 위해 정렬한다.
data = list(map(str, data))             # 출력에서 시간을 줄이기 위해 str로 변형한다.

print('\n'.join(map(' '.join, combinations(data, m))))

# My Solution2(dfs, 72ms)
'''
dfs로도 풀어봤다.
현재 인덱스보다 큰 인덱스를 뽑아주면 되므로 
visited 리스트를 만들어 방문여부를 확인할 필요가 없다. 무조건 다른 수들만 뽑기 때문이다.
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
    
    for i in range(now+1, n):           # 오름차순이므로 now+1~n까지를 탐색한다.
        result.append(data[i])          # 해당 인덱스의 데이터를 result에 넣어준다.
        dfs(i, count+1)                 # dfs를 수행한다.
        result.pop()                    # 해당 인덱스를 이용한 조합은 모두 탐색했으므로 result에서 뺀다.

dfs(-1, 0)