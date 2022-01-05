# My solution(80ms)
n, m = map(int, input().split()) # 1 ≤ M ≤ N ≤ 8

'''
자연수 N과 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오.
1. 1부터 N까지 자연수 중에서 M개를 고른 수열
2. 같은 수를 여러 번 골라도 된다.
3. 고른 수열은 비내림차순이어야 한다.
   길이가 K인 수열 A가 A1 ≤ A2 ≤ ... ≤ AK-1 ≤ AK를 만족하면, 비내림차순이라고 한다.

위 조건은 이전 수보다 무조건 크거나 같은 수를 뽑으면 해결이 가능하다.
'''

result = []
def dfs(now, count):
    if count == m:                          # m개의 숫자를 뽑았다면
        print(' '.join(map(str, result)))   # result를 출력한다.
        return                              # 숫자를 더 이상 뽑을 필요가 없으므로 함수를 종료한다.

    for i in range(now, n+1):               # 아직 m개를 뽑지 못했으므로 반복문을 사용해 숫자를 뽑아준다.(이전에 뽑은 수보다 크거나 같은 수를 뽑아준다.)
        result.append(i)                    # result에 i를 추가한다.
        dfs(i, count+1)                     # 현재 뽑은 수를 i로 하고 dfs를 실행한다.
        result.pop()                        # 현재 i를 뽑는 모든 경우를 출력했을 것이다. 따라서 i를 빼내주고 반복문으로 돌아간다.

dfs(1, 0)