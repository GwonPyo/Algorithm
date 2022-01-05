# My Solution(68ms)
'''
임의의 정수 n을 1, 2, 3의 합으로 나타내려면 1차원 리스트를 이용한 dynamic programming을 이용해 해결할 수 있다.
dp를 이용하면 아래와 같은 규칙을 가진다.
* dp[n] = dp[n-1]+dp[n-2]+dp[n-3]
n-1을 만들 수 있는 식의 마지막에 1을 더하면 n을 만들 수 있으며
n-2, n-3을 만들 수 있는 식들에는 2, 3을 더하면 n을 만들 수 있다.
따라서 위와 같은 점화식을 이용해 코드를 작성하면 문제를 해결할 수 있다.
'''
import sys
input = sys.stdin.readline

dp = [0 for _ in range(11)]         # n은 0보다 크고 11보다 작으므로 1~10까지의 수들만 값을 갱신해주면 된다.
dp[1] = 1                           # n이 1, 2, 3인 경우는 미리 갱신한다.
dp[2] = 2
dp[3] = 4

for i in range(4, 11):              # n이 4~10까지인 경우를 갱신한다.
    dp[i] = dp[i-1]+dp[i-2]+dp[i-3] # 점화식은 위에서 말한 식과 동일하다.

for _ in range(int(input())):       # 테스트 케이스만큼 반복한다.
    n = int(input())                # 정수 n(0<n<11)을 입력받고 알맞은 값을 출력한다.
    print(dp[n])