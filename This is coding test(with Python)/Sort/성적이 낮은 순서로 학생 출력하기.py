n = int(input())

result = []
for _ in range(n):
    name, score = input().split()
    result.append((name, int(score)))

result.sort(key = lambda x: x[1])

for i in result:
    print(i[0], end = ' ')