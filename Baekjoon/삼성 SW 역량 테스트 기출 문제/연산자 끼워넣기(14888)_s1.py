# My Solution1 (브루트포스, 2700ms) - Python 제출시 시간초과
import sys
from itertools import permutations

input = sys.stdin.readline

def calculator(operator, a, b):                             # 계산기 역할을 하는 함수를 만들어준다.
    if operator == '+':
        return a+b
    elif operator == '-':
        return a-b
    elif operator == '*':
        return a*b
    else:
        if a < 0:
            return -((-a)//b)
        else:
            return a//b


n = int(input())                                            # 숫자 리스트의 수를 받아온다.
nums = list(map(int, input().split()))                      # 리스트를 받아준다.
operators = [['+'], ['-'], ['*'], ['/']]            
operators_num = list(map(int, input().split()))             # +, -, //, *를 사용할 수 있는 개수를 의미한다.
operators_list = []

for operator, num in zip(operators, operators_num):         # permutations에 사용할 리스트를 만들기위해 +, -, *, /로 이루어진 리스트를 만든다.
    operators_list += operator*num

operators_perms = list(permutations(operators_list, n-1))   # 위에서 만든 리스트로 순열을 만들어준다.

max = float('-inf')
min = float('inf')

for operators in operators_perms:                           # 모든 경우를 탐색해본다.
    result = nums[0]
    for index, operator in enumerate(operators):
        index = index+1
        result = calculator(operator, result, nums[index])
    
    if result > max: max = result
    if result < min: min = result

print(max)
print(min)

# My Solution2 (백트래킹, 184ms) 
import queue
import sys
input = sys.stdin.readline
    
n = int(input())
nums = list(map(int, input().split()))         
operators_limit = list(map(int, input().split()))                   # +, -, //, *를 사용할 수 있는 개수를 의미한다.
operators_visited = [0 for _ in range(4)]                           # 각 연산자의 사용 횟수를 체크하는 리스트다.

maximum = float('-inf')                                             # maximum과 minimum을 각각 음의 무한대와 양의 무한대로 설정한다.
minimum = float('inf') 

def calculator(operator, a, b):                                     # 계산기 역할을 하는 함수를 만들어준다.
    if operator == 0:
        return a+b
    elif operator == 1:
        return a-b
    elif operator == 2:
        return a*b
    else:
        return int(a/b)

def dfs(ex_result, depth):                                          # 백트래킹을 수행하는 함수다.
    global maximum, minimum
    if depth >= len(nums):                                          # 주어진 연산을 마무리하면
        maximum = max(maximum, ex_result)                           # 최대값과 최소값을 비교해 갱신해준다.
        minimum = min(minimum, ex_result)
        
    for i in range(4):                                              # 연산을 마무리하지 못했다면
        if operators_visited[i]<operators_limit[i]:                 # 사용가능한 연산자를 찾아 수행해준다.
            operators_visited[i] += 1
            dfs(calculator(i, ex_result, nums[depth]), depth+1)
            operators_visited[i] -= 1

dfs(nums[0], 1)
print(maximum)
print(minimum)