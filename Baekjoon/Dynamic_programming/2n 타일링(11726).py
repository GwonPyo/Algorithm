n = int(input())
result = [1, 2] + [0] * (n - 2)

for i in range(2, n):
    result[i] = result[i - 1] + result[i - 2]

print(result[n - 1] % 10007)