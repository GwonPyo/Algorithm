# My Solution1(permuataions, 100ms)
'''
수열의 조건은 다음과 같다.
1.N개의 자연수 중에서 M개를 고른 수열 (단, N개의 자연수는 모두 다른 수이다.)

data 리스트로 n개의 숫자를 저장하고 사전순으로 출력하기 위해 정렬하면 된다.
그리고 출력을 위해 문자열로 바꿔준 후 permutations 함수를 사용해 만들 수 있는 모든 순열을 만들면 문제를 해결할 수 있다. 
먼저 str로 바꿔버리면 '10000'같은 문자가 제대로 정렬되지 않아 int형태에서 정렬해야 한다.(str상태에서 정렬하면 사전순으로 정렬되기 때문이다.)
'''
from itertools import permutations
import sys
input = sys.stdin.readline

n, m = map(int, input().split())        # n: 총 숫자의 개수, m: 결과를 구성할 숫자의 개수
data = list(map(int, input().split()))  # data를 입력받는다.
data.sort()                             # 사전순으로 출력하기 위해 정렬한다.
data = list(map(str, data))             # 출력에서 시간을 줄이기 위해 str로 변형한다.

for result in permutations(data, m):            
    print(' '.join(result))             # 결과들을 출력한다.

'''
아래는 다른 사람의 풀이에서 가져온 출력 방식이다.
해당 방식의 속도가 더 빨랐다. 앞으로 이런 방식의 출력도 고려해보자.
'''
print('\n'.join(map(' '.join, permutations(data, m)))) # 80ms

# My Solution2(dfs, 152ms)
'''
정석대로 dfs로도 풀어봤다.
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
        if not visited[i]:              # 해당 인덱스를 방문하지 않았다면
            visited[i] = True           # 방문처리를 해준다.
            result.append(data[i])      # result에 해당 인덱스의 숫자를 추가해준다.
            dfs(count+1)                # dfs를 수행한다.
            visited[i] = False          # 탐색을 완료했으므로 미방문 처리를 한다.(순열을 만들기 위해서는 이후에도 방문해야 한다.)
            result.pop()                # result에서 해당 인덱스의 숫자를 빼준다.
dfs(0)