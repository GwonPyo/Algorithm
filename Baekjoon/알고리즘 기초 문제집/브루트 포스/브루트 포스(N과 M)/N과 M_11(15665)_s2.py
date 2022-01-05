# My Solution1(product, 128ms)
'''
수열의 조건은 다음과 같다.
1. N개의 자연수 중에서 M개를 고른 수열
2. 같은 수를 여러 번 골라도 된다.

같은 수를 여러 번 골라도 된다.
따라서 중복된 데이터를 한 개만 남기고 지워도 아무런 문제가 없다.
그래서 set함수를 이용해 중복된 데이터를 지워주고 list형으로 바꿔 정렬해줬다.
그리고 product함수를 사용하면 중복 순열을 구할 수 있으므로 문제를 해결할 수 있다.
'''
from itertools import product

n, m = map(int, input().split())            # n: 총 숫자의 개수, m: 결과를 구성할 숫자의 개수
data = list(set(map(int, input().split()))) # 데이터를 입력받고, 중복되는 데이터는 지워준다.
data.sort()                                 # 사전순으로 출력하기 위해 정렬한다.
data = list(map(str, data))                 # 출력에서 시간을 줄이기 위해 str로 변형한다.

print('\n'.join(map(' '.join, product(data, repeat=m))))


# My Solution2(dfs, 328ms)
'''
dfs로도 풀어봤다.
조건이 이해가 안된다면 N과 M(9)를 참고하자.
'''
n, m = map(int, input().split())            # n: 총 숫자의 개수, m: 결과를 구성할 숫자의 개수
data = list(map(int, input().split()))      # data를 입력받는다.
data.sort()                                 # 사전순으로 출력하기 위해 정렬한다.
data = list(map(str, data))                 # 출력에서 시간을 줄이기 위해 str로 변형한다.

result = []                                 # 결과를 담을 리스트다.
def dfs(count):
    if count == m:                          # m개의 수를 뽑았다면
        print(' '.join(result))             # 결과를 출력하고 함수를 종료한다.
        return

    prev = 0                                # 이전에 사용한 데이터를 저장할 변수다.
    for i in range(n):                      # 데이터를 중복해서 고를 수 있으므로 0~n-1까지 탐색한다.
        if prev != data[i]:                 # 해당 인덱스의 데이터가 이전에 사용한 데이터가 아니라면
            result.append(data[i])          # result에 해당 데이터를 넣어준다.
            dfs(count+1)                    # dfs를 수행한다.
            result.pop()                    # 해당 데이터를 포함한 모든 경우를 탐색했기 때문에 result에서 빼준다.
            prev = data[i]                  # 이전에 사용한 데이터를 갱신한다.
dfs(0)

# My Solution3(dfs, 304ms)
'''
dfs를 이용한 두 번째 풀이다.
Solution1과 같이 중복되는 데이터를 미리 지울 수 있다.
따라서 중복되는 데이터를 지워주고 dfs를 이용해 
조건(if prev != data[i]:)을 사용하지 않고 중복 순열을 구했다.
'''
n, m = map(int, input().split())
data = list(set(map(int, input().split())))
data.sort()
data = list(map(str, data))

result = []
def dfs(count):
    if count == m:
        print(' '.join(result))
        return
    
    for i in range(len(data)):
        result.append(data[i])
        dfs(count+1)
        result.pop()
dfs(0)
