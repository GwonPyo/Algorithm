import sys
input = sys.stdin.readline
# 입력할 정수의 개수 k
k = int(input())
# 반환할 값 result
result = 0
# k개의 정수 입력
stack = []
for _ in range(k):
    n = int(input())
    # 입력받은 정수가 0이 아니면 stack에 입력
    if n != 0:
        stack.append(n)
    # 입력받은 정수가 0이면 바로 이전에 입력받은 값 삭제    
    # 이 원리가 선입선출 구조이므로 stack을 사용했다.
    else:
        stack.pop()

print(sum(stack))