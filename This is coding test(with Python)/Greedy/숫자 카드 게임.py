N, M = map(int, input().split())

result = 0

for _ in range(N):
    data = list(map(int, input().split()))
    target = min(data)
    result = max(result, target)

print(result)