# My solution(1672ms)
'''
자연수 N과 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오.
1. 1부터 N까지 자연수 중에서 M개를 고른 수열
2. 같은 수를 여러 번 골라도 된다.

그냥 매번 1~n까지 하나의 숫자를 골라주면 된다.
더 빠르게 하려면 itertools 라이브러리를 사용하면 된다.
'''
n, m = map(int, input().split()) # 1 ≤ M ≤ N ≤ 7

def dfs(count, result):
    if count == m:                          # m개 만큼 뽑았다면
        print(' '.join(map(str, result)))   # 해당 조합을 출력한다.
        return                              # 더 뽑을 필요가 없으므로 함수를 종료한다.
    for i in range(1, n+1):                 # m개 만큼 뽑지 않았다면 숫자를 더 뽑아야 한다.
        result.append(i)                    # result에 i를 추가해준다.
        dfs(count+1, result)                # i를 포함한 조합에서 dfs를 수행한다.
        result.pop()                        # 해당 숫자를 포함한 조합들을 모두 출력했으므로 해당 숫자를 result에서 빼준다.

dfs(0, [])