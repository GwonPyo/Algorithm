# My Solution(80ms)
'''
우리가 가지고 있는 타일은 다음과 같다.
=> 1×2, 2×1 타일
n번째 정수의 결과값을 구할때 고려할 경우는 2가지가 있다.
1) 마지막 부분이 2*1 1개의 블럭으로 채워진 경우
2) 마지막 부분이 1*2 2개의 블럭으로 채워진 경우
위 케이스를 가지고 점화식을 만들면
dp[n] = dp[n-1] + dp[n-2] 가 된다.
해당 점화식을 이용해 코드를 구현했다.
'''

n = int(input())                # 1 ≤ n ≤ 1,000
dp = [0, 1, 2] + [0] * (n-2)    # 정수 1과 2의 결과값은 미리 지정해 주고 나머지 값은 반복문을 이용해 갱신해준다.

for i in range(3, n+1):         # 3~n까지의 값을 갱신한다.
    dp[i] = dp[i-1]+dp[i-2]     # 점화식을 이용해 정수 i의 결과값을 갱신한다.

print(dp[n]%10007)              # 2*n 크기의 직사각형을 채우는 방법의 수를 10,007로 나눈 나머지를 출력한다.

