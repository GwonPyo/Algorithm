import sys
import math
input = sys.stdin.readline

# 1 <= N, M <= 9
N, M = map(int, sys.stdin.readline().split())

numbers = []
for _ in range(N):
    numbers.append(list(map(int, list(input().rstrip()))))

result = -1

for n in range(N): # 시작할 행(n)
    for m in range(M): # 시작할 행(m)
        for weight_n in range(-N, N): # 행의 공차.
            for weight_m in range(-M, M): # 열의 공차.
                # 두 공차가 모두 0이면 무한 루프가 발생한다.
                if weight_n == 0 and weight_m == 0: 
                    continue
                x = n
                y = m
                value = ''
                # 입력받은 수들의 범위 안에서 가능한 수열 추출
                while (0 <= x < N) and (0 <= y < M):
                    value += str(numbers[x][y]) # 숫자를 조합한다.

                    value_int = int(value) # 현재 value값을 정수형으로 변형한다.
                    value_sqrt = math.sqrt(value_int) # 루트를 씌운다.
                    value_decimal = value_sqrt - int(value_sqrt) # 완전 제곱수라면 값이 0이 나올 것이다.
                    if value_decimal == 0 and value_int > result: 
                        # value_dicimal의 값이 0이고 변수 result에 저장된 값보다 크면 result에 value_int를 저장한다.
                        result = value_int

                    # x에 공차를 더한다.
                    x += weight_n
                    # y에 공차를 더한다.
                    y += weight_m

print(result)

'''
행과 열이 최대 9밖에 안되기 때문에 완전 탐색을 사용하기로 결정했다.
위와 같은 방법으로 풀면 된다고는 생각했지만 구현을 하기가 어려워 다른
사람의 코드를 이용했다. 꼭 몇 번 복습하기로 하자.
'''