n, k = map(int, input().split())
# 일차원 리스트 이용한 구현
dp = [1 for _ in range(n + 1)]

for j in range(2, k + 1):
    for i in range(1, n + 1):
        # 점화식
        # dp[i]는 이전 dp[0]~dp[i]의 합을 구하면 된다.
        # 이때 dp[0]~dp[i - 1] 까지의 합은 dp[i - 1]로 이전에 계산된 값이다.
        # 따라서 dp[i - 1]과 dp[i]를 저장해주면 된다.
        dp[i] = (dp[i] + dp[i - 1]) % 1000000000
# 처음에는 위 반복문을 2 ~ k - 1번만 반복했다. + dp에 1,000,000,000으로 나눈 값을 넣지 않았다.
# 위 방식으로 풀면 결국 print에 sum(dp)를 하게 되는데 이때 오버플로우가 발생되는 것 같다.
# 따라서 k까지 모두 반복해주고 dp에도 결과 값에 1,000,000,000을 나눈 값을 넣어주면 정답이 나온다.
print(dp[n])


# 이중 리스트(dp)를 이용한 구현
dp = [[1 for _ in range(n + 1)] for _ in range(k + 1)]

for i in range(2, k + 1):
    for j in range(1, n + 1):
        dp[i][j] = dp[i - 1][j] + dp[i][j - 1] 
# 1,000,000,000으로 나눈값을 넣지 않아도 정답으로 나온다.
# 하지만 다음 문제부턴 나누어 주는게 좋을 뜻 하다.
print(dp[k][n] % 1000000000)

