import sys
input = sys.stdin.readline

'''
강의 왼쪽과 오른쪽에 각각 n개와 m개의 사이트가 있고,
각 사이트를 이어 다리를 만들어야 한다. 단, 다리가 겹치면 안 된다.
즉, 오른쪽 m개의 사이트중 n개를 골라서 알아서 이어주면 된다.
따라서 조합 공식을 그대로 사용하면 된다. 
mCn = m! / ((m-n)! * n!)
'''
# dp로 팩토리얼을 구현한다.
dp = [1 for _ in range(31)]
for i in range(2, 31):
    dp[i] = i * dp[i - 1]

# 테스트 케이스만큼 반복한다.
for _ in range(int(input())):
    # 0 < 왼쪽 사이트(n) <= 오른쪽 사이트(m) < 30
    n, m = map(int, input().split())
    # 저장된 팩토리얼 값을 이용해 계산해준다.
    print(dp[m] // (dp[m-n] * dp[n]))