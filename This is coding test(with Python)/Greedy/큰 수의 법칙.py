N, M, K = map(int, input().split())
# N: 배열의 크기. 
# M: 더해지는 횟수
# K: 같은 수를 더할 수 있는 최대 횟수

numbers = list(map(int, input().split()))
# 숫자 입력 받음

numbers.sort(reverse = True)

result = (numbers[0] * K + numbers[1]) * (M // (K + 1)) + numbers[0] * (M % (K + 1))
print(result)