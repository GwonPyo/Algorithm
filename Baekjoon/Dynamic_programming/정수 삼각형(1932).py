import sys
input = sys.stdin.readline


n = int(input())
triangle = []

for _ in range(n):
    triangle.append(list(map(int, input().split())))

# 하향식
# 처음에는 루트에서 시작하면 된다고 생각했다.
for i in range(1, n):
    # 부모에서 시작하면 경우는 두가지로 나뉜다.
    for j in range(i + 1):
        # 1) 부모가 한 개인 경우(즉, 배열의 양 끝 / j == 0, j == i)
        if j == 0:
            triangle[i][j] = triangle[i - 1][j] + triangle[i][j]
        elif j == i:
            triangle[i][j] = triangle[i - 1][j - 1] + triangle[i][j]
        # 2) 부모가 두 개인 경우(배열 양 끝을 제외한 나머지)
        # 해당 인덱스가 j라면 부모는 윗행의 j - 1, j이다.
        else:
            triangle[i][j] = max(triangle[i - 1][j - 1] + triangle[i][j], triangle[i - 1][j] + triangle[i][j])

print(max(triangle[n - 1]))

n = int(input())
triangle = []

for _ in range(n):
    triangle.append(list(map(int, input().split())))
# 상향식
# 하향식과는 다르게 리프에서 시작했다.
# 하향식 방식이 생각보다 복잡해서 상향식으로 바꾸어 생각해보았다.
for i in range(n - 1, 0, - 1):
    # 상향식은 무조건 한 가지만 고려하면 된다.
    for j in range(i):
        # 부모로 올라 갈때
        # 부모 입장에서는 두 자식중 더 큰 자식을 선택하면 된다.
        # 부모의 인덱스가 j라면 자식들의 인덱스는 j, j + 1이 된다.
        if triangle[i][j] > triangle[i][j + 1]:
            triangle[i - 1][j] += triangle[i][j]
        else:
            triangle[i - 1][j] += triangle[i][j + 1]
print(triangle[0][0])