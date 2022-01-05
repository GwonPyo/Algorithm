# 주사위로 n^3 정육면체를 만들어야 한다.
# n을 입력받는다.
n = int(input())

# a, b, c, d, e, f를 입력받는다.
# a는 f
# b는 e
# c는 d
# 와 마주본다.
a, b, c, d, e, f = map(int, input().split())

if n == 1:
    # n이 1인 경우를 처리하지 않아 한 번 틀렸다.
    # 알고리즘 문제를 풀땐 사소한거라도 조심하자.
    print(a + b + c + d + e + f - max(a, b, c, d, e, f))

else:
    # 마주보는 면과 비교해 더 작은 값을 구한다.
    min_values = [min(a, f), min(b, e), min(c, d)]
    min_values.sort()

    # 정육면체의 한 변의 길이는 n이다
    # 정사각형의 안쪽 부분에는 min_values의 가장 작은 값(min_values[0])으로 채워 넣으면된다. (총 (n - 2) * (n - 2))
    # 정사각형의 안쪽과 모서리를 제외한 부분은 주사위의 두 면만 보인다. 따라서 min_values의 가장 큰 값을 제외한
    # 나머지 부분(min_values[0] + min_values[1])만 보이게 되도록 만든다.
    # 정사각형의 모서리는 세면(sum(min_values))이 모두 보인다.
    # 모든 합을 구해 나올 수 있는 면중 최대값을 구해 빼주면된다.
    inside = min_values[0] * ((n - 2) * ((n - 2))) * 6
    outside_not_edge = (min_values[0] + min_values[1]) * (n - 2) * 12
    edge = sum(min_values) * 8
    max_side = min_values[0] * ((n - 2) * (n - 2)) + min_values[1] * (n - 2) * 4 + min_values[2] * 4

    print(inside + outside_not_edge + edge - max_side)

# 다른 풀이를 보면 비슷한 풀이거나 위 수식을 한 번에 계산하고 풀었다. 원리는 같다.