# My Solution1(dfs, 72ms)
'''
수열의 조건은 아래와 같다.
1. N개의 자연수 중에서 M개를 고른 수열이다.
2. 고른 수열은 비내림차순이어야 한다.
(길이가 K인 수열 A가 A1 ≤ A2 ≤ ... ≤ AK-1 ≤ AK를 만족하면, 비내림차순이라고 한다.)

데이터가 중복되어 주어질 수 있으므로 이전에 N과 M(9) 문제에서 사용했던 방식을 쓰면 쉽게 풀 수 있다.
비내림차순이지만 같은 수를 여러 번 사용할 수 있다는 조건이 없으므로 이전에 탐색한 인덱스+1(now+1)~n까지 탐색해야 한다.
해당 함수 내에서 이전에 사용한 데이터가 현재 인덱스의 원소(데이터)와 같다면 탐색하지 않으면 된다.
'''

import sys
input = sys.stdin.readline

n, m = map(int, input().split())                                # n: 총 숫자의 개수, m: 결과를 구성할 숫자의 개수
data = list(map(int, input().split()))                          # data를 입력받는다.
data.sort()                                                     # 사전순으로 출력하기 위해 정렬한다.
data = list(map(str, data))                                     # 출력에서 시간을 줄이기 위해 str로 변형한다.

result = []
def dfs(now, count):                                            
    if count == m:                                              # m개의 수를 뽑았다면
        print(' '.join(result))                                 # 결과를 출력하고 함수를 종료한다.
        return

    prev = 0                                                    # 이전에 사용한 데이터를 저장할 변수다.        
    for i in range(now+1, n):                                   # now+1~n까지 탐색한다.
        if prev != data[i]:                                     # 이전에 사용한 데이터가 아니라면
            result.append(data[i])                              # result에 해당 인덱스의 데이터를 추가한다.
            dfs(i, count+1)                                     # dfs를 수행한다.
            result.pop()                                        # 해당 인덱스의 데이터를 뽑았을 때의 경우는 모두 탐색했으므로 result에서 빼준다. 
            prev = data[i]                                      # 이전에 사용한 데이터를 갱신한다.

dfs(-1, 0) 