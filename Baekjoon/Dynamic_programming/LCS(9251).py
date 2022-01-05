# 문자열 1, 2입력
str1 = input()
str2 = input()
# LCS알고리즘에 이용할 dp 생성
# 열: str1, 행: str2
dp = [[0 for _ in range(len(str1) + 1)] for _ in range(len(str2) + 1)]
# LCS 알고리즘 실행
for row in range(1, len(str2) + 1):
    # str2의 길이 만큼 실행
    for column in range(1, len(str1) + 1):
        # str1의 길이 만큼 실행 
        # 즉 str1의 각 문자를 현재 str2의 문자 한개와 비교
        if str2[row - 1] == str1[column - 1]:
            # 현재 str1의 문자와 str2의 문자가 같으면 실행
            dp[row][column] = dp[row - 1][column - 1] + 1
        else:
            # 현재 str1의 문자와 str2의 문자가 다르면 실행
            dp[row][column] = max(dp[row][column - 1], dp[row - 1][column])
# 마지막 행의 마지막 열 원소 출력
print(dp[-1][-1])

# 다른 사람 코드
import sys

def getLCS(str1, str2):
    x = len(str1)
    y = len(str2)
    dp = [0] * 1000

    for i in range(x):
        temp = 0
        for j in range(y):
            if temp < dp[j]: temp = dp[j]
            elif str1[i] == str2[j]: dp[j] = temp + 1
    
    return max(dp)

string_1 = sys.stdin.readline().strip()
string_2 = sys.stdin.readline().strip()
print(getLCS(string_1, string_2))