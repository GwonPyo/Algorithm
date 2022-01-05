import sys
input = sys.stdin.readline

n = int(input())
RGB_costs = [(0, 0 ,0)]
R, G, B = 0, 1, 2
for _ in range(n): 
    RGB_costs.append(list(map(int, input().split())))

# 열: R, G, B 각각의 최솟값을 구하기 위해 총 3개 생성
dp = [[0 for _ in range(3)] for _ in range(n + 1)]

dp[1] = RGB_costs[1]

for i in range(2, n + 1):
    # 현재 위치에서 R을 고르려면
    # 이전 위치에서 G혹은 B를 골라야한다.
    # 따라서 이전 G, B중 작은 값을 골라 더하면 된다.
    # G, B도 동일한 방식으로 진행한다.
    dp[i][R] = min(dp[i - 1][G] + RGB_costs[i][R], dp[i - 1][B] + RGB_costs[i][R])
    dp[i][G] = min(dp[i - 1][R] + RGB_costs[i][G], dp[i - 1][B] + RGB_costs[i][G])
    dp[i][B] = min(dp[i - 1][R] + RGB_costs[i][B], dp[i - 1][G] + RGB_costs[i][B])

# 맨 마지막 행에서의 최소값을 출력한다.
print(min(dp[n]))