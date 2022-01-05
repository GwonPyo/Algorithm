import sys
input = sys.stdin.readline
# n: 물품의 수, k: 버틸 수 있는 무게
n, k = map(int,input().split())
# items: 아이템의 무게, 가치를 저장하는 리스트
items = [[0, 0]]
# 이중 리스트인 dp 생성(행: 0 ~ n(물건의 개수), 열: 0 ~ k(버틸 수 있는 무게))
dp = [[0 for _ in range(k + 1)] for _ in range(n + 1)]

for _ in range(n):
    items.append(tuple(map(int, input().split())))

for i in range(1, n + 1):
    # i: 아이템의 개수(행의 개수) 만큼 반복
    for j in range(1, k + 1):
        # j: 버틸 수 있는 무게
        weight = items[i][0] # 해당 물건(행)의 무게
        value = items[i][1] # 해당 물건(행)의 가치

        if j < weight:
            # 물건의 무게가 버틸 수 있는 무게보다 크다면
            # 이전 j에서의 최대 가치 값을 불러온다.
            dp[i][j] = dp[i - 1][j]
        else:
            # 물건의 무게가 버틸 수 있는 무게보다 작다면
            # 이전 j(현재 버틸 수 있는 무게) - weight(물건의 무게)의 최대 가치와 현재 물건의 가치를
            # 이전 j의 최대 가치와 비교하여
            # 더 큰 값을 j의 최대 가치로 넣어준다.
            dp[i][j] = max(value + dp[i - 1][j - weight], dp[i - 1][j])

print(dp[n][k])
