# My Solution(240ms)
'''
임의의 2*n 배열에서 사자를 배치하는 경우의 수는
2*(n-1) 배열에서 사자를 배치하는 경우의 수에서 약간의 변형이 필요하다.

해당 경우는 3가지의 case로 나눌 수 있다.
1. 이전 층이 0, 1일 때는 (0, 0) & (1, 0) 이 다음 층에 올 수 있다.
2. 이전 층이 1, 0일 때는 (0, 0) & (0, 1) 이 다음 층에 올 수 있다.
3. 이전 층이 0, 0일 때는 (0, 0) & (0, 1) & (1, 0) 이 다음 층에 올 수 있다.
[1은 사자가 들어 있다는 의미이다.]

따라서 2차원 리스트 형태의 dp를 만들면 dynamic programming을 통해 개수를 효율적으로 셀 수 있다.
[1차원 리스트로도 가능하다.(이전의 층의 수치만 사용하기 때문이다.)]
'''
n = int(input())
dp = [[1, 1, 1]] + [[0, 0, 0] for _ in range(n-1)]      # 각 열의 원소는 해당 층이 (0, 1), (1, 0), (0, 0)인 경우의 수를 나타낸다.

for i in range(1, n):                                   # 2*n 층까지 값을 갱신한다. 아래는 위 설명에 기반한 점화식이다.
    dp[i][0] = (dp[i-1][1]+dp[i-1][2]) % 9901
    dp[i][1] = (dp[i-1][0]+dp[i-1][2]) % 9901
    dp[i][2] = (dp[i-1][0]+dp[i-1][1]+dp[i-1][2]) % 9901

print(sum(dp[n-1])%9901)                                # 결과를 출력한다.

# Other Solution(88ms)
'''
각 층마다 값은 아래와 같다.
N   ans
1   3
2   7
3   17
4   41

해당 수들의 규칙을 점화식으로 나타내면 다음과 같다.
dp[n] = dp[n-1] * 2 + dp[n-2]
해당 점화식을 코드로 나타내면 다음과 같다.
'''
a,b = 1,3
n = int(input())
for i in range(2,n+1):
    a, b = b, (b*2 + a)%9901
print(b)
