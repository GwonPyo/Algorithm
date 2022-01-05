# 숫자를 담은 리스트(numbers)
numbers = list(map(int, list(input())))

'''
우리가 선택할 연산은 1. 곱하기, 2. 더하기 두 개이다.
간단히 생각해보면 0 혹은 1은 더해야 하고,
이외의 숫자는 곱하는 것이 더 큰 수가 나온다.
즉, 앞에 있는 수와 뒤에 있는 수가 1 이하인지 초과인지 확인해야 한다.
'''

for index in range(len(numbers) - 1):
    a = numbers[index]
    b = numbers[index + 1]
    # 두 수가 둘다 1보다 크면 곱한다.
    if a > 1 and b > 1:
        numbers[index + 1] = a * b
    # 두 수중 하나라도 1 이하면 더해준다.
    else:
        numbers[index + 1] = a + b

print(numbers[-1])

'''
풀이 시간: 5분

계산 결과를 변수를 생성해 저장하는 방법이 아니라 배열의 다음 원소에 저장하는 방법을 사용했다.
따라서 맨 마지막 원소에 결과가 저장되어 number[-1]을 출력했다.
아래와 같이 코드를 바꿔봤는데 더 읽기 편한 것 같다. 시간 복잡도는 동일하다.
책은 아래 코드와 거의 동일하다.
'''

result = numbers[0]

for number in numbers[1:]:
    if result > 1 and number > 1:
        result *= number
    else:
        result += number

print(result)

