# My Solution1(오답)
'''
그리디로 풀 수 있을 거라는 생각이 들었지만 그렇지 않았다.
처음에 모든 수를 0으로 초기화하고 결과에 맞는 가장 작은 수들로 구성되게 했다.
예를 들어,
-+-+--라는 입력이 들어 왔다고 하자.
1. -1 0  0 (처음 부호가 -이므로 -1) 
2. -1 2  0 (지금까지 결과가 -1인데 부호는 +이므로 2)
3. -1 2 -2 (지금까지 결과가 1인데 부호는 -이므로 -2)
4. -1 2 -2 (해당 숫자가 2이고 부호는 +이므로 갱신하지 않는다.)
5. -1 2 -3 (지금까지 결과가 2인데 부호는 -이므로 -3)
6. -1 2 -3 (해당 숫자가 -3이고 부호는 -이므로 갱신하지 않는다.)
식으로 진행된다.
하지만 아래처럼 반례가 존재한다.
(입력)
-++++-
(출력)
1. -, [-1, 0, 0]
2. +, [-1, 2, 0]
3. +, [-1, 2, 0]
4. +, [-1, 2, 0]
5. +, [-1, 2, 0]
6. -, [-1, 2, -1]
로 틀린 답이 나오게 된다. 
'''
n = int(input())                                    # 숫자의 개수를 입력받을 변수다.
arr = list(input())                                 # 부호를 입력받을 리스트이다.

result = [0 for _ in range(n)]                      # 숫자 조합을 저장할 리스트다.

count = 0                                           # 부호에 알맞게 접근하기 위한 변수다.
for x in range(n, 0, -1):
    memory = 0                                      # 우리가 더하는 구간합을 임시로 저장할 변수다.
    for y in range(x):
        index = count + y                           # arr에 알맞게 접근하기 위해 count와 y를 더해서 인덱스를 만들어 준다.
        
        if arr[index] == '+':                       # 현재 구간을 포함한 결과는 양수인데 지금까지 결과가 양수가 아닌 경우
            if result[n-x+y] + memory <= 0:
                result[n-x+y] = 1-memory            # 현재 값을 양수로 만들어 준다. (메모리의 절대값보다 1크게 만든다.)
            memory += result[n-x+y]                 # memory에 해당 값을 더한다.
            
        elif arr[index] == '-' and memory >= 0:     # 현재 구간을 포함한 결과는 음수인데 지금까지 결과가 음수가 아닌 경우
            if result[n-x+y] + memory >= 0: 
                result[n-x+y] = -1-memory           # 현재 값을 음수로 만들어 준다. (메모리의 절대값의 음수보다 1작게 만든다.)
            memory += result[n-x+y]                 # memory에 해당 값을 더한다.
            

        elif arr[index] == '0':                     # 현재 구간을 포함한 결과가 0이라면
            result[n-x+y] = memory * (-1)           # 현재까지 구간합에 음수를 취해준다.
            memory = 0                              # memory에는 0을 저장한다.                 
    count += x                                      # x만큼 count에 더해준다.

print(' '.join(map(str, result)))                   # 최종 결과를 출력한다.

# My Solution2(메모리 초과)
'''
해당 코드는 아래 과정으로 동작된다.
1. 먼저 각 숫자의 부호를 확인한다. (확인후 signs 리스트에 저장함.)
2. 0~n-1까지의 부등호에 만족하는지 확인하면서 임의로 정한 숫자 조합을 results에 저장한다.
3. results에 저장된 조합들이 다른 조건에 만족하는지 확인해본다.
'''
n = int(input())                                                # 숫자의 개수를 입력받는다.
arr = list(input())                                             # 부호를 입력받는다.

signs = []                                                      # 각 숫자의 부호를 저장할 리스트다.
count = 0                                                       # 이전 코드와 같이 올바른 인덱스에 접근하기 위해 사용할 변수다.
for i in range(n, 0, -1):                                       # 숫자의 개수만큼 반복한다.                           
    index = count                                               # 각 구간합의 첫 번째 원소가 해당 원소의 인덱스가 된다. ex) 0번째 원소의 부호는 0, 1번째 원소의 부호는 n에 저장되어 있다.
    signs.append(arr[index])                                    # signs를 갱신한다.
    count += i

results = []                                                    # 결과(result)를 담을 리스트다.
def dfs(now, memory, result):                                   # now: 찾고 있는 원소의 인덱스, memory: 현재까지 구간합의 결과, result: 결과를 담을 리스트
    if now == n:                                                # n개의 숫자를 모두 찾았다면
        results.append(result)                                  # results에 result를 추가한다.(메모리 초과의 원인)
        return                                              
    
    if signs[now] == '0':                                       # 현재 숫자가 0이라면 조건문을 수행한다.
        if arr[now] == '+' and memory <= 0: return              # 이전까지의 합이 현재의 조건에 맞지 않으면 종료한다.
        elif arr[now] == '-' and memory >= 0: return
        elif arr[now] == '0' and memory != 0: return
        else: dfs(now+1, memory, result+[0])                    # 조건에 맞는다면 dfs를 이어서 수행한다.
        
    elif signs[now] == '+':                                     # 현재 부호가 +라면 조건문을 수행한다.
        for i in range(1, 11):                                  # 1~10까지 탐색한다.
            if  arr[now] == '+' and memory+i <= 0: continue     # 탐색한 수와 이전의 합을 더했을 때 조건에 맞지 않으면 반복문으로 돌아간다.
            elif arr[now] == '-' and memory+i >= 0: break
            elif arr[now] == '0' and memory+i != 0: continue
            else: dfs(now+1, memory+i, result+[i])              # 조건에 맞는다면 dfs를 수행한다.
            
    elif signs[now] == '-':                                     # 현재 부호가 -라면 조건문을 수행한다.
        for i in range(-10, 0):                                 # -1~-10까지 탐색한다.
            if  arr[now] == '+' and memory+i <= 0: continue     # 탐색한 수와 이전의 합을 더했을 때 조건에 맞지 않으면 반복문으로 돌아간다.
            elif arr[now] == '-' and memory+i >= 0: break
            elif arr[now] == '0' and memory+i != 0: continue
            else: dfs(now+1, memory+i, result+[i])              # 조건에 맞는다면 dfs를 수행한다.

dfs(0, 0, [])

for result in results:                                          # results에 저장된 결과들을 하나씩 꺼내 확인한다.        
    count = n                                                   # 0~n-1까진 이미 확인했기 때문에 확인할 필요가 없다. 따라서 count는 이전과 다르게 n으로 초기화한다.
    check = 0                                                   # check는 부호가 틀린것이 있는지 확인하기 위한 변수다.
    for x in range(1, n):                                       
        memory=0                                                # 구간합을 저장할 변수다.
        for y in range(n-x):                                    
            index = count+y                                     # index를 알맞게 지정해준다.
            memory += result[x+y]                               # result에 알맞은 값에 접근하여 memory에 더해준다.

            # 더한 값이 조건에 맞지 않으면, check를 -1로 초기화하고 반복문을 종료한다.
            if (memory >= 0 and arr[index] == '-') or (memory <= 0 and arr[index] == '+') or (memory != 0 and arr[index] == '0'):
                check = -1
                break

        if check == -1: break                                   # 조건에 맞지 않으면 반복문을 종료한다.
        count += n-x                                            # 모든 조건에 맞았다면 반복문으로 돌아가 올바른 인덱스에 접근하기 위해 n-x를 더해준다.
    if check == -1:                                             # 조건에 맞지 않았다면
        check = 0                                               # check를 다시 0으로 초기화하고
        continue                                                # 반복문으로 돌아간다.
    print(' '.join(map(str, result)))                           # 올바른 결과가 있다면 출력한다.
    break                                                       # 결과는 하나만 출력하면 되므로 이대로 종료한다.
    
# My Solution3(시간초과)
'''
메모리 초과 부분을 고쳐서 코드를 다시 제출했다. 이번에는 시간 초과가 발생했다.
코드 작동은 동일하게 완전 탐색으로 풀었다.
'''
n = int(input())
arr = list(input())

signs = []

# n개의 숫자의 부호를 판단한다.
count = 0
for i in range(n, 0, -1):
    index = count
    signs.append(arr[index])
    count += i

results = []
def dfs(now, memory, result):
    '''
    메모리 초과 코드에서 results의 원소를 하나씩 뽑아 다른 부등호에 만족하는지 확인했던 방식을
    now == n일때 확인해서 사용할 메모리를 줄였다. (위에서는 results에 result를 append해 줬다.)
    '''
    if now == n:                                                
        count = n                                               
        for x in range(1, n):
            memory=0
            for y in range(n-x):
                index = count+y
                memory += result[x+y]
                if memory >= 0 and arr[index] == '-': return    # 현재 값을 더했을 때, 조건에 맞지 않으면 반복문을 종료한다.
                elif memory <= 0 and arr[index] == '+': return  # 현재 값을 더했을 때, 조건에 맞지 않으면 반복문을 종료한다.
                elif memory != 0 and arr[index] == '0': return  # 현재 값을 더했을 때, 조건에 맞지 않으면 반복문을 종료한다.
            count += n-x
        print(' '.join(map(str, result)))
        exit()
    
    if signs[now] == '0':                                       # 현재 숫자가 0이라면 조건문을 수행한다.
        if arr[now] == '+' and memory <= 0: return              # 이전까지의 합이 현재의 조건에 맞지 않으면 종료한다.
        elif arr[now] == '-' and memory >= 0: return
        elif arr[now] == '0' and memory != 0: return
        else: dfs(now+1, memory, result+[0])                    # 조건에 맞는다면 dfs를 이어서 수행한다.
        
    elif signs[now] == '+':                                     # 현재 부호가 +라면 조건문을 수행한다.
        for i in range(1, 11):                                  # 1~10까지 탐색한다.
            if  arr[now] == '+' and memory+i <= 0: continue     # 탐색한 수와 이전의 합을 더했을 때 조건에 맞지 않으면 반복문으로 돌아간다.
            elif arr[now] == '-' and memory+i >= 0: break
            elif arr[now] == '0' and memory+i != 0: continue
            else: dfs(now+1, memory+i, result+[i])              # 조건에 맞는다면 dfs를 수행한다.
            
    elif signs[now] == '-':                                     # 현재 부호가 -라면 조건문을 수행한다.
        for i in range(-10, 0):                                 # -1~-10까지 탐색한다.
            if  arr[now] == '+' and memory+i <= 0: continue     # 탐색한 수와 이전의 합을 더했을 때 조건에 맞지 않으면 반복문으로 돌아간다.
            elif arr[now] == '-' and memory+i >= 0: break
            elif arr[now] == '0' and memory+i != 0: continue
            else: dfs(now+1, memory+i, result+[i])              # 조건에 맞는다면 dfs를 수행한다.

dfs(0, 0, [])

# Other Solution1(python: 6900ms / pypy: 804ms)
'''
위와 같이 백트래킹을 통해 완전탐색을 수행하려고 할 때,
수행 시간을 줄이는 핵심 방법은 탐색을 멈출 조건을 잘 정해주는 것 밖에 없다고 생각한다.
즉, 위 코드에서는 0~n-1의 조건만을 확인해 가능한 조합을 찾고 나머지 부등호가 맞는지 확인해줬다.
하지만 다른 부등호를 더 고려해서 조합을 찾는다면, 이후 부등호가 맞는지 확인할 필요가 없고, 조건을 통해 탐색을 조금 더 빨리 종료할 수 있을 것이다.
아래 방법은 이러한 방법을 이용한 코드이다.

나는 부호를 입력받고, 그냥 1차원 배열을 사용해 문제를 풀었다.
이래도 되긴하지만 문제에서는 
"S[i][j]는 A[i]부터 A[j]까지 합이 0보다 크면 +, 0이면 0, 0보다 작으면 -이다."
라는 문항이 있다.
문제에서 이러한 말들을 꼭 주의해서 보는게 좋은 것 같다.
아래 코드처럼 2차원으로 배열을 만들면 접근이 훨씬 편해진다.

위와 같이 2차원 배열로 접근이 가능해지면 ck() 함수처럼 더 많은 부등호를 고려해 탐색 지속 여부를 판단할 수 있다.
S[i][idx]는 i~idx의 구간합을 의미한다.
'''
def ck(idx):
    hap = 0                                     # 구간합을 저장할 변수다.
    for i in range(idx, -1, -1):                # idx~0까지 탐색한다.
        hap += result[i]                        # idx원소부터 하나씩 더해 구간합을 갱신해준다.
        if hap == 0 and S[i][idx] != 0:         # 구간합이 부등호에 만족하지 않으면
            return False                        # False를 반환한다.
        elif hap < 0 and S[i][idx] >= 0:        # 구간합이 부등호에 만족하지 않으면
            return False                        # False를 반환한다.
        elif hap > 0 and S[i][idx] <= 0:        # 구간합이 부등호에 만족하지 않으면
            return False                        # False를 반환한다.
    return True                                 # 모든 부등호를 만족하면 True를 반환한다.

def solve(idx):                                 # dfs를 수행한다.
    if idx == N:                                # n개의 숫자를 모두 찾았다면
        return True                             # True를 반환한다.
    if S[idx][idx] == 0:                        # 해당 숫자의 부호가 0이라면
        result[idx] = 0                         # 해당 원소에 0을 저장한다.
        return solve(idx+1)                     # 다음 원소를 기준으로 다시 dfs를 수행한다.
    for i in range(1, 11):                      # 1~10까지 탐색한다.
        result[idx] = S[idx][idx] * i           # S에는 +이면 +1, -이면 -1이 저장되어 있다. 따라서 S[idx][idx] * i를 수행하면 올바른 값을 탐색한다.
        if ck(idx) and solve(idx+1):            # ck(idx)가 참이고 solve(idx+1)이 참이라면
            return True                         # True를 반환한다.
    return False                                # 올바른 값이 없다면 False를 반환한다.

N = int(input())
arr = list(input())
S = [[0]*N for i in range(N)]                   # 부호를 이차원 배열 형태로 담을 것이다.
for i in range(N):                              # 0~n-1행에 접근한다.
    for j in range(i, N):                       # i~n-1열에 접근한다.
        temp = arr.pop(0)                       # pop(0)을 사용하면 deque의 popleft처럼 왼쪽부터 원소를 꺼내준다.
        if temp == '+':                         # 부호가 +라면 
            S[i][j] = 1                         # 1을 저장한다.
        elif temp == '-':                       # 부호가 -라면
            S[i][j] = -1                        # -1을 저장한다.

result = [0] * N                                # 숫자를 담을 배열을 생성한다.
solve(0)                                        # solve함수를 이용해 result를 갱신한다.(올바른 결과를 찾으면 바로 함수가 종료된다.)
print(' '.join(map(str, result)))               # result의 값을 출력한다.

# Other Solution1 + My Solution(python:시간초과 / pypy: 940ms)
'''
위 방식을 내 코드로 바꿔보았다.
하지만 python상에서는 시간초과가 되었다. 다른 방식도 찾아봐야 할 것같다.
원리는 위 코드와 동일하다. 이해가 안된다면 위 코드를 살펴보자.
'''
from collections import deque
n = int(input())
arr = deque(input())
data = [[0 for _ in range(n)] for _ in range(n)]
result = [0] * n
for i in range(n):
    for j in range(0, n-i):
        a = arr.popleft()
        if a == '+': data[i][j+i] = 1
        elif a == '-': data[i][j+i] = -1

def check(now):
    memory = 0
    for i in range(now, -1, -1):
        memory += result[i]
        if data[i][now] == 0 and memory != 0: return False
        elif data[i][now] == 1 and memory <= 0: return False
        elif data[i][now] == -1 and memory >= 0: return False
    return True

def dfs(now):
    if now == n:
        print(' '.join(map(str, result)))       # 위 코드에서는 return True를 하고 함수를 종료해 마지막에 출력해줬다.
        exit()                                  # 하지만 내 코드에서는 출력 후 exit()를 사용해 바로 종료해주므로 상관이 없다. 
    if data[now][now] == 0:
        result[now] = 0
        if check(now): dfs(now+1)
    else: 
        for i in range(1, 11):
            result[now] = data[now][now]*i
            if check(now): dfs(now+1)           # return True를 이용해 봤지만 똑같이 python에서 시간 초과가 발생한다.
dfs(0)

# Other Solution2(72ms)
'''
기본적으로 사용한 알고리즘은 동일하게 완전 탐색을 사용했다.
다른점은 기존에는 열을 기준으로 탐색했다면 해당 코드는 행을 기준으로 탐색한다.
-++-
 +++
  --
   -
라는 입력이 있었다고 하자.
이전까지의 코드는 3번째 원소를 탐색할 때 - -> + -> +를 탐색했다.
하지만 해당 코드는 - -> -를 탐색한다.
'''

n = int(input())                                        # 숫자의 개수를 입력받는다.
string = input()                                        # 부호를 입력받는다.
b = 0                                                   # 지금까지 계산한 구간합의 개수를 저장할 변수다.
a = n                                                   # 구간합의 개수를 저장할 변수다.
x = []
positive = [1, 10, 3, 8, 2, 9, 4, 7, 5, 6]              # 양수로 가능한 값을 리스트로 만들어 놓는다.(1~10)
negative = [-i for i in positive]                       # 음수로 가능한 값을 리스트로 만들어 놓는다.(-1~-10)
zero = [0]                                              # 0일때 가능한 값을 리스트로 만들어 놓는다.(0)

while a:                                                # a의 개수(n)만큼 반복해 부호를 2차원으로 저장한다.
    x.append(string[b:b + a])                           # b~b+a-1까지의 부호를 저장한다.
    b += a                                              # b에 a를 더한다.
    a -= 1                                              # 구간합의 개수는 1씩 감소하므로 a값에 1을 뺀다.
y = {'+':positive, '-':negative, '0': zero}             # dictionary를 이용해 부호(key)에 따른 value값을 지정한다.
pool = []
for row in x:                                           # x에는 각 구간합의 부호들이 저장되어 있다. 해당 문자열들을 하나씩 꺼낸다.
    pool.append(y[row[0]])                              # 문자열의 맨 앞은 해당 index 원소의 부호를 의미한다. 따라서 pool에는 해당 부호에 맞는 리스트를 저장한다.
y = {'+':set(positive), '-':set(negative), '0': {0}}    
v = [0]*n                                               # 숫자를 저장할 리스트다.
flag = False                                            # 숫자가 만들어졌는지 확인할 때 사용할 변수다. 
def dfs(i, s):                                          
    global flag                                         # flag를 global처리한다.
    if flag:                                            # flag가 True라면 함수를 종료한다.
        return
    if i == -1:                                         # 만약 i가 -1이라면 
        flag = True                                     # flag에 True값을 지정하고
        print(*v)                                       # 결과를 출력한다.
        return                                          # 그리고 함수를 종료한다.
    for j in pool[i]:                                   # pool[i]에 저장된 값을 탐색한다.
        v[i] = j                                        # v[i]에 해당 값을 넣는다.
        a = 0                                           
        t = s + j                                       # 이전까지 구간값(s)에 현재 탐색값(j)을 더한다.
        for k in range(n - 1, i, -1):                   # n-1~i까지 탐색한다.
            if t - a not in y[x[i][k-i]]:               # 현재값을 포함한 전체 구간값(t)에 a를 뺀 결과값이 해당 부호(key)에 해당하는 value값안에 없다면 
                break                                   # 반복문을 종료한다.
            a += v[k]                                   # a에 검사한 인덱스의 값을 더해준다.
        else:                                           # 모든 값이 만족했다면
            dfs(i-1, t)                                 # 다음 원소의 dfs를 수행한다.
dfs(n-1, 0)                                             # 맨 끝값부터 탐색을 시작한다.

#Other Solution2 + My Solution(python: 1940ms)
'''
이번에는 위 코드와 같이 열이 아니라 행으로 비교했다.
원리상 차이는 별로없지만 데이터상 행으로 비교하는 것이 더 빠른 것 같다.
'''
from collections import deque
n = int(input())
arr = deque(input())
data = [[0 for _ in range(n)] for _ in range(n)]
result = [0] * n
for i in range(n):
    for j in range(0, n-i):
        a = arr.popleft()
        if a == '+': data[i][j+i] = 1
        elif a == '-': data[i][j+i] = -1

def check(now, value):
    for i in range(n-1, now, -1):
        if data[now][i] == 0 and value != 0: return False
        elif data[now][i] == 1 and value <= 0: return False
        elif data[now][i] == -1 and value >= 0: return False
        value -= result[i]
    return True

def dfs(now, value):
    if now == -1:
        print(' '.join(map(str, result)))               
        exit()                                          
    if data[now][now] == 0:
        result[now] = 0
        if check(now, value): dfs(now-1, value)
    else: 
        for i in range(1, 11):
            result[now] = data[now][now]*i      
            if check(now, value+result[now]): dfs(now-1, value+result[now])           
dfs(n-1, 0)