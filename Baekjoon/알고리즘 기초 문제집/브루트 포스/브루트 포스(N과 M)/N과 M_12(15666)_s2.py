# My Solution(72ms)
'''
수열의 조건은 다음과 같다.
1. N개의 자연수 중에서 M개를 고른 수열
2. 같은 수를 여러 번 골라도 된다.
3. 고른 수열은 비내림차순이어야 한다.

같은 수를 여러 번 골라도 된다.
따라서 중복되는 데이터가 주어지면 해당 데이터들을 하나만 남기고 지우고
조건에 만족하는 수열을 만들면 된다.
'''
n, m = map(int, input().split())            # n: 총 숫자의 개수, m: 결과를 구성할 숫자의 개수
data = list(set(map(int, input().split()))) # 데이터를 입력받고, 중복되는 데이터는 지워준다.
data.sort()                                 # 사전순으로 출력하기 위해 정렬한다.
data = list(map(str, data))                 # 출력에서 시간을 줄이기 위해 str로 변형한다.

result = []                                 # 결과를 담을 리스트다.
def dfs(now, count):    
    if count == m:                          # m개의 숫자를 뽑았다면
        print(' '.join(result))             # 결과를 출력하고 함수를 종료한다.
        return

    for i in range(now, len(data)):         # 비내림차순이므로 이전에 사용한 인덱스(now)~data의 개수(len(data))를 탐색하면 된다.
        result.append(data[i])              # result에 해당 인덱스의 데이터를 넣어준다.
        dfs(i, count+1)                     # dfs를 수행한다.
        result.pop()                        # 해당 데이터를 이용한 모든 경우의 탐색이 완료되었으므로 result에서 빼준다.

dfs(0, 0)

# My Solution2(72ms)
'''
중복된 데이터를 지우지 않고 풀 수 있다.
조건이 이해되지 않는다면 N과 M(9)문제를 참고하자.
'''
n, m = map(int, input().split())            # n: 총 숫자의 개수, m: 결과를 구성할 숫자의 개수
data = list(map(int, input().split()))      # data를 입력받는다.
data.sort()                                 # 사전순으로 출력하기 위해 정렬한다.
data = list(map(str, data))                 # 출력에서 시간을 줄이기 위해 str로 변형한다.

result = []                                 # 결과를 저장할 리스트다.
def dfs(now, count):                        
    if count == m:                          # m개의 수를 뽑았다면
        print(' '.join(result))             # 결과를 출력하고 함수를 종료한다.
        return

    prev = 0                                # 이전에 사용한 데이터를 저장할 변수다.
    for i in range(now, n):                 # 비내림차순이므로 이전에 사용한 인덱스(now)~n-1을 탐색하면 된다.
        if prev != data[i]:                 # 해당 인덱스의 데이터가 이전에 사용한 데이터가 아니라면
            result.append(data[i])          # result에 넣어준다.
            dfs(i, count+1)                 # dfs를 수행한다.
            result.pop()                    # 해당 데이터를 이용한 모든 경우의 탐색이 완료되었으므로 result에서 빼준다.
            prev = data[i]                  # 이전에 사용한 데이터를 갱신한다.

dfs(0, 0)

# My Solution3(84ms)
'''
비내림차순이고 같은 수를 여러번 고를 수 있다면,
중복되는 수를 1개씩만 나두고 중복 조합을 수행하면 된다.
즉, combinations_with_replacement 함수를 사용하면 된다. 
'''

from itertools import combinations_with_replacement
n, m = map(int, input().split())            # n: 총 숫자의 개수, m: 결과를 구성할 숫자의 개수
data = list(set(map(int, input().split()))) # 데이터를 입력받고, 중복되는 데이터는 지워준다.
data.sort()                                 # 사전순으로 출력하기 위해 정렬한다.
data = list(map(str, data))                 # 출력에서 시간을 줄이기 위해 str로 변형한다.

print('\n'.join(map(' '.join, combinations_with_replacement(data, m))))