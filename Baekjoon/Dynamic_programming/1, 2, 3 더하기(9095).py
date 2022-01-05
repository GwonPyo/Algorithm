import sys
sys_input = sys.stdin.readline

test_num = int(input())
test_cases = []

for _ in range(test_num):
    test_cases.append(int(sys_input()))

dp = [0, 1, 2, 4] + [None] * 8

for test_case in test_cases:
    for i in range(test_case + 1):
        if dp[i] == None:
            dp[i] = dp[i - 3] + dp[i - 2] + dp[i - 1]
    print(dp[test_case])