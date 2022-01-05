# 문자열 입력
str1 = input()
str2 = input()
# LCS에 사용할 dp 생성
dp = [[0 for _ in range(len(str1) + 1)] for _ in range(len(str2) + 1)]

# LCS 알고리즘 실행
for row in range(1, len(str2) + 1):
    for column in range(1, len(str1) + 1):
        if str2[row - 1] == str1[column - 1]:
            dp[row][column] = dp[row - 1][column - 1] + 1
        else:
            dp[row][column] = max(dp[row][column - 1], dp[row - 1][column])

# LCS 길이 출력
row, column = -1, -1
print(dp[row][column])

# LCS 문자열 생성
lcs = []
while dp[row][column] > 0:
    while dp[row][column] == dp[row - 1][column]:
        row -= 1
    while dp[row][column] == dp[row][column - 1]:
        column -= 1
    lcs.append(str1[column])
    row -= 1; column -= 1
lcs.reverse()
print(''.join(lcs))