#My Solution(144ms)
'''
dynamic programming을 이용해 풀었다.
원리는 '카드 구매하기(11052)_s1.py'를 참고하자.
'''
import sys
input = sys.stdin.readline

n = int(input())                            # 1 ≤ N ≤ 1,000
dp = [0]+list(map(int, input().split()))    # 1 ≤ Pi ≤ 10,000

def find_min(n):                            # 각 케이스의 최솟값을 dp에 저장해주는 함수다.
    for i in range(1, n//2+1):              # pi가 이미 저장되어 있으므로 n//2번만 반복해주면 된다.
        dp[n] = min(dp[n], dp[i]+dp[n-i])   # 이미 저장되어 있는 값과 계산해야할 값을 비교해 더 작은 값을 dp에 저장한다.

for i in range(n+1):                        # 0~n까지 모든 dp를 갱신한다.(사실 반복은 2에서 부터 시작해도 무방하다.)
    find_min(i)                             

print(dp[n])                                # 최종 결과값을 출력한다. 
