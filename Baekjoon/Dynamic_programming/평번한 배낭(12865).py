import sys
input = sys.stdin.readline
'''
n: 물품 개수, limit: 준서가 버틸 수 있는 무게
items: 각 물건의 무게와 가치를 담는 리스트
'''
n, limit = map(int, input().split()) 
items = list([(0, 0)]) 

# (무게, 가치)를 입력받고 items리스트에 넣어준다.
for _ in range(n):
    items.append(tuple(map(int, input().split())))

# dp table을 생성해준다.
dp = [[0 for _ in range(limit+1)] for _ in range(n+1)]

# knapsack 알고리즘을 수행한다.
for row in range(1, n+1):
    weight, value = items[row]
    for col in range(1, limit+1):
        if weight <= col:
            dp[row][col] = max(dp[row-1][col], dp[row-1][col-weight]+value)
        else:
            dp[row][col] = dp[row-1][col]

# dp의 마지막 원소를 출력한다.
print(dp[-1][-1])