# My Solution1(652ms)
'''
정수 x에 사용할 수 있는 연산은 다음과 같이 세 가지 이다.

1. x가 3으로 나누어 떨어지면, 3으로 나눈다.
2. x가 2로 나누어 떨어지면, 2로 나눈다.
3. 1을 뺀다.

0~n까지 모든 숫자의 결과값을 구해 마지막 n값을 구하는 방식을 사용했다.(Bottom-Up 방식)
점화식은 간단하다.
먼저 1을 뺀 결과를 dp에 임시로 저장한다.
2로 나눠지는 수라면 2로 나눈 결과와 이전 결과를 비교해 더 작은 값을 dp에 저장한다.
3으로 나눠지는 수라면 3으로 나눈 결과와 이전 결과를 비교해 더 작은 값을 dp에 저장한다.
'''

n = int(input())                                        # 정수 n을 입력받는다. (1 <= n <= 10^6)
dp = [0 for _ in range(n+1)]                            # 0~n까지의 인덱스를 가진 list를 만든다.

for i in range(2, n+1):                                 # dp의 2~n까지의 인덱스를 가진 원소들을 갱신하기 위해 2~n까지 반복한다.
    dp[i] = dp[i-1]+1

    if i % 2 == 0:                                      # 2로 나누어 떨어진다면
        dp[i] = min(dp[i], dp[i//2]+1)                  # 해당 수를 2로 나누었을 때의 결과와 이전 결과를 비교해 더 작은 값을 저장한다.

    if i % 3 == 0:                                      # 3으로 나누어 떨어진다면
        dp[i] = min(dp[i], dp[i//3]+1)                  # 해당 수를 3으로 나누었을 때의 결과와 이전 결과를 비교해 더 작은 값을 저장한다.

print(dp[n])

#Other Solution(60ms)
'''
내 코드는 상향식으로 풀었지만 아래 코드는 재귀함수를 이용해 하향식으로 구현했다.(Top-Down 방식)
정수 n의 결과를 구할 때는 아래와 같이 수행한다.
1. n을 2로 나누어질 때까지 빼준값과 n//2의 결과값을 더한다.
2. n을 3으로 나누어질 때까지 빼준값과 n//3의 결과값을 더한다.
3. 더 작은 값에 1을 더하고 해당 값을 갱신해준다.

더 빠른 이유는 '필요한 값의 결과값만 구하기 때문'인 것 같다.
상향식은 모든 값을 구하면서 n번 반복해야 결과를 구할 수 있다.
하지만 하향식은 필요한 값들만 구하면서 결과값을 구할 수 있으므로 시간 복잡도는 동일해도 시간이 많이 절약되는 것 같다.
'''
def dp(n):
    if n in memo:                                       # 이미 구한 결과값이라면
        return memo[n]                                  # 해당 값을 반환한다.
    
    m = 1 + min(dp(n // 2) + n % 2, dp(n // 3) + n % 3) # 각 결과값을 비교해 최소값에 1을 더한다.
    memo[n] = m                                         # 결과값을 가지고 있는 리스트를 갱신한다.
    return m                                            # 결과값을 반환한다.


memo = {1: 0, 2: 1}                                     # 결과값을 저장할 dictionary이다.
n = int(input())                                        # 정수 n을 입력받는다.
print(dp(n))                                            # dp 함수를 실행해 결과값을 출력한다.
