import sys 
input = sys.stdin.readline

n = int(input())
# range(n)으로 리스트 생성시
# n = 0 일 때 에러 발생
stairs = [0 for _ in range(300)]
dp = [0 for _ in range(300)]

for i in range(n):
    stairs[i] = int(input())

dp[0] = stairs[0]
dp[1] = stairs[0] + stairs[1]
dp[2] = max(stairs[1] + stairs[2], stairs[0] + stairs[2])
# 계단 알고리즘
# 1. 한칸 전 계단을 밟고 올라온 경우.
# 2. 두칸 전 계단을 밟고 온 경우.
for i in range(3, n):
    dp[i] = max(dp[i - 3] + stairs[i - 1] + stairs[i], dp[i - 2] + stairs[i])

print(dp[n - 1])