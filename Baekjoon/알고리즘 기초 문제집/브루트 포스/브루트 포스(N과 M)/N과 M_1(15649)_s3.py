# My solution(160ms)

'''
처음 봤을 때는 반복문을 사용해서 풀려고 했다.
하지만 m에 따라 반복해야 하는 횟수가 다르다. 따라서 반복문으로 풀 수는 없다고 생각했다.
그래서 dfs를 생각했다.
그래프를 탐색하는 것은 아니지만 탐색과정이 dfs와 다를바 없다고 생각했다.

코드는 아래의 과정으로 진행된다.
1.  1~n중 하나를 고르고 해당 위치를 방문처리한다. 그리고 result에 문자열을 저장한다.
2.  만약 m만큼 뽑았다면 result를 출력한다. 
    시작점을 제외하고 1~n중 하나를 선택한다. 해당 위치를 방문처리하고 문자열에 추가한다.
3.  m개 만큼 뽑았다면 result를 출력한다.
    뽑았던 점들을 제외하고 1~n중 하나를 선택한다. 해당 위치를 방문처리하고 문자열에 추가한다.
(위 과정 반복)
수열의 조건은 아래와 같다.
(조건) 1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열
즉 뽑은 수의 순서는 상관없으므로 1~n까지 안 뽑았던 수만 뽑아주면 된다.
'''
n, m = map(int, input().split()) # 1 <= m <= n <=8
visited = [False for _ in range(n+1)] # 방문 확인

# dfs
def dfs(now, count, result):
    # m개 만큼 뽑았다면 result 출력하고 함수를 종료한다.
    # 함수를 종료하지 않으면 계속 반복되므로 꼭 종료해야 한다.
    if count == m:
        print(result)
        return
    
    # m개 만큼 뽑지 않았다면 뽑지 않은 수 중에서 하나를 뽑고, dfs를 수행한다.
    for i in range(1, n+1):
        if not visited[i]:
            visited[i] = True
            dfs(i, count+1, result+" "+str(i))
            visited[i] = False

# 처음 숫자를 고르고 dfs를 수행해준다.
for i in range(1, n+1):
    visited[i] = True
    result = str(i)
    dfs(i, 1, result)
    visited[i] = False

# Other Solution1(240ms)
n, m = map(int, input().split()) # 수를 입력받는다.

s = [] # 지금까지 뽑은 수들을 저장한다.

def f(): 
    # m개 만큼 뽑았다면 s를 출력하고 함수를 종료한다.
    if len(s) == m:
        print(' '.join(map(str, s)))
        '''
        숫자를 원소로 가지는 s의 모든 원소를 str type으로 바꾸려면 아래와 같이 작업할 수 있다.
        list(map(str, s))
        '''
        return

    # 1~n까지 숫자 한 개를 뽑는다.
    for i in range(1, n + 1):
        # 이미 뽑은 숫자라면 다시 뽑는다.
        if i in s:
            continue
        # 뽑은 숫자가 아니라면 s에 추가한다.
        s.append(i)
        # 함수를 다시 실행한다.
        f()
        s.pop()
f()

# Other Solution2(76ms, itertools 모듈 사용)
'''
permutation: 순열
nPr과 같이 고등학생 때 배웠던 순열을 의미한다.
위 문제의 조건이 순열을 찾는 것과 동일하므로 해당 함수를 써도 문제가 없다.
permutations(n개의 원소를 가진 array, r(뽑을 개수))
식으로 사용하면 모든 조합을 추출해준다.
'''
from itertools import permutations

N, M = map(int, input().split())
# 1~n까지의 수를 먼저 문자열로 바꿔준다.
li = map(str, range(1, N+1))

'''
a = [["1", "2"], ["1", "2"]]
a = list(map(' '.join, a))
의 결과는 
['1 2', '1 2']이다.
'''
print('\n'.join(list(map(' '.join,permutations(li, M)))))