# My Solution1(product, 304ms)
'''
수열의 조건은 다음과 같다
1. N개의 자연수 중에서 M개를 고른 수열 (단, N개의 자연수는 모두 다른 수이다.)
2. 같은 수를 여러 번 골라도 된다.

같은 수를 여러 번 골라도 된다면, 중복 순열을 사용하면 된다.
따라서 중복 순열을 만들어주는 product함수를 사용했다.
'''

from itertools import product
import sys
input = sys.stdin.readline

n, m = map(int, input().split())        # n: 총 숫자의 개수, m: 결과를 구성할 숫자의 개수
data = list(map(int, input().split()))  # data를 입력받는다.
data.sort()                             # 사전순으로 출력하기 위해 정렬한다.
data = list(map(str, data))             # 출력에서 시간을 줄이기 위해 str로 변형한다.
'''
product함수는 permutations, combinations와 다르게
product(data, m) 방식으로 쓰면 error가 발생한다.
이때 product(data, repeat=m) 방식으로 쓰면 원하는 결과를 출력할 수 있다. (repeat 매개변수를 꼭 적어줘야 한다.)
'''
print('\n'.join(map(' '.join, product(data, repeat=m))))


# My Solution2(dfs, 864ms)
'''
dfs로도 풀어봤다.
각 dfs마다 모든 수를 탐색하면 된다.
즉, 이전에 풀었던 순열 문제의 dfs에서 visited를 빼주면 된다.
'''
import sys
input = sys.stdin.readline

n, m = map(int, input().split())        # n: 총 숫자의 개수, m: 결과를 구성할 숫자의 개수
data = list(map(int, input().split()))  # data를 입력받는다.
data.sort()                             # 사전순으로 출력하기 위해 정렬한다.
data = list(map(str, data))             # 출력에서 시간을 줄이기 위해 str로 변형한다.

visited = [False for _ in range(n)]     # 방문처리를 위한 리스트를 생성한다.
result = []                             # 결과를 저장할 리스트다.
def dfs(count):                     
    if count == m:                      # m개의 숫자를 뽑았다면
        print(' '.join(result))         # result를 출력하고 함수를 종료한다.
        return

    for i in range(n):                  # m개의 숫자를 뽑지 않았다면 0~n-1을 모두 탐색한다.
        result.append(data[i])          # result에 해당 인덱스의 숫자를 추가해준다.
        dfs(count+1)                    # dfs를 수행한다.
        result.pop()                    # result에서 해당 인덱스의 숫자를 빼준다.

dfs(0)