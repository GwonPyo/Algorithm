# my_solution
import sys
input = sys.stdin.readline

'''
1, 2, 3으로 숫자를 만들어야 한다.
따라서 어떤 n이라는 숫자를 만드려면
n-1 + 1
n-2 + 2
n-3 + 3
을 하면 된다.
따라서 n-1, n-2, n-3의 경우의 수를 모두 더해주면 n을 만들 수 있는 경우의 수를 구할 수 있다.
'''

dp = [0 for _ in range(12)]
# 1, 2, 3은 미리 설정해준다.
dp[1] = 1
dp[2] = 2
dp[3] = 4
# n은 1~11까지의 수만 가능하다. 따라서 4~11까지 반복하면서 dp를 채운다.
for i in range(4, 12):
    dp[i] = dp[i-1] + dp[i-2] + dp[i-3]

for _ in range(int(input())):
    n = int(input()) # 1, 2, 3으로 만드려고 하는 수, 0 < n < 11
    print(dp[n]) # n번째 원소를 반환한다.