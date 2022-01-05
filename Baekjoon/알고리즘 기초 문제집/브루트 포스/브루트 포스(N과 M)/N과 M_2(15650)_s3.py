# My Solution(68ms)

'''
N과 M_1의 조건과 유사하지만 '오름차순'이라는 조건이 추가되었다.
(조건)
1. 1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열
2. 고른 수열은 오름차순이어야 한다.
그래서 이전과 코드가 비슷하지만 뽑은 수보다 무조건 큰 수만 뽑게 했다.
'''
n, m = map(int, input().split()) # 숫자 입력

# dfs 수행
def dfs(now, count, result):
    # m개를 뽑았다면 result 출력후 종료
    if count == m:
        print(result)
        return
    # 사실 range(now+1, n+1)로 써도 아무런 문제가 없다.
    for i in range(now+1, n-m+2+count):
        # 현재 수보다 큰 수를 뽑고 dfs 수행
        # 현재 수보다 큰 수만 뽑으므로 이전처럼 방문 여부를 확인할 필요가 없다.
        dfs(i, count+1, result+" "+str(i))
# 처음 숫자를 뽑는다.
for i in range(1, n-m+2):
    result = str(i)
    dfs(i, 1, result)

# Other Solution(68ms)
n,m = list(map(int,input().split())) # 숫자 입력
s = [] # 뽑은 숫자를 담을 리스트
def dfs(start):
    # m개 만큼 뽑았다면 s 출력
    if len(s)==m:
        print(' '.join(map(str,s)))
        return
    # m개 만큼 뽑지 못했다면 숫자를 뽑는다.
    # 단, start보다 큰 수를 뽑는다.
    for i in range(start,n+1):
        # 조건문은 start를 거르기 위한 조건문인 것 같다.
        if i not in s:
            s.append(i)
            dfs(i+1)
            s.pop()
dfs(1)