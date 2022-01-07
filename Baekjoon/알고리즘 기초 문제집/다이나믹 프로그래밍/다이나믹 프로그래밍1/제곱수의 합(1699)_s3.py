# My Solution(7484ms)
'''
임의의 수 n을 제곱수 합으로 표현하는데 필요한 제곱수 항의 최소 개수를 구해야 한다.
n의 루트값의 절대값이 a라고 하자.
이때, 1~a의 제곱값(i)을 n에 빼주면 이전에 n-i에서 구한 제곱수 항의 최소 개수(dp[n-i])에 1을 더해 n의 최소값을 구할 수 있다.
점화식은 다음과 같다.
dp[n] = min(dp[n], dp[n-i]+1) [i는 1~a의 제곱수다.]
'''

from math import sqrt
n = int(input())
dp = [i for i in range(n+1)]                        # dp값에 인덱스와 동일한 값으로 초기화하면 해당 정수를 표현하는데 필요한 제곱수 항의 최대 개수가 된다.(모두 1의 제곱으로 이루어 진 것이기 때문이다.)
square = [i * i for i in range(1, int(sqrt(n))+1)]  # 제곱수 항이 될 수 있는 모든 제곱수를 저장한다.


for i in range(2, n+1):                             # n이 1일 때 값은 1이기 때문에 2부터 n까지 값을 갱신해야 한다.
    tmp = int(sqrt(i))                              # i의 제곱근을 저장한다. (사용할 수 있는 최대 제곱수를 알기 위함이다.)
    for j in square[:tmp]:                          # 1~최대 제곱수를 모두 사용해 제곱수 항의 최소 개수를 구한다.
        dp[i] = min(1+dp[i-j], dp[i])

print(dp[n])                                        # 구한 값을 출력한다.

# Other Solution(4884ms)
'''
내 코드의 원리와 동일하지만 내 코드처럼 매번 dp[i]와 값을 비교하는 것이 아니라 리스트 s에 저장해서 한 번에 구한다.
'''
n = int(input())
dp = [0 for i in range(n + 1)]                      # 내 코드의 dp역할과 같다.
square = [i * i for i in range(1, 317)]             # 1~317를 제곱한 수를 미리 저장해 둔다.(내 코드는 1~루트n를 제곱한 수를 미리 저장했다.)
for i in range(1, n + 1):                           # 1~n까지의 수를 탐색하면서 값을 갱신한다.
    s = []                                          # 각 제곱수 합의 항 개수를 저장할 리스트다.
    for j in square:                                # 제곱수가 i보다 작으면
        if j > i:
            break
        s.append(dp[i - j])                         # 내 코드의 원리와 동일하게 dp[i-j]값을 리스트에 저장한다.
    dp[i] = min(s) + 1                              # s에 저장된 값중 가장 작은 값에 1을 더한 값을 저장한다.
print(dp[n])                                        # 구한 값을 출력한다.


