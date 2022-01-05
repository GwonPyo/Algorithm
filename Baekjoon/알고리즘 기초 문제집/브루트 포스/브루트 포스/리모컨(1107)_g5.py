# my solution(748ms)
import sys
input = sys.stdin.readline

n = int(input()) # 이동하려는 채널 (0 <= n <= 500,000)
m = int(input()) # 고장난 버튼의 개수 (0 <= m <= 10)
buttons = []     # 눌리지 않는 버튼을 저장할 리스트
# 고장난 버튼이 없다면 아래 조건문을 실행하지 않는다.
if m > 0:
    buttons = list(input().split())

'''
수빈이는 현재 채널 100번에 있다.
따라서 이동하려는 채널과 100채널 사이의 차이값이 가장 기본값이라고 볼 수 있다.
해당 값을 result에 저장한다.
'''
result = abs(n - 100)

# 먼저 고장난 버튼이 없다면, 해당 채널의 번호를 입력하기만 하면 된다.
if not buttons:
    result = min(result, len(str(n))) # 따라서 기본값과 채널의 길이(len(str(n)))를 비교하면 된다.


#모두 고장났다면 무조건 기본값이 정답이다.
elif len(buttons) == 10: pass

# 만약 가려고 하는 채널이 100보다 작거나 같다면(0~100) 해당 조건문을 실행한다
elif n <= 100:
    # n~0까지 즉, n보다 작거나 같은 채널이 눌리는지 확인한다.
    for i in range(n, -1, -1): 
        can_click = True # 아래 반복문이 실행되고 can_click이 계속 True라면 해당 채널을 입력할 수 있다.
        for button in buttons:
            # 고장난 버튼이 채널에 포함되면 해당 채널을 클릭할 수 없다.
            if button in str(i):
                can_click = False
                break
        # 해당 채널을 입력할 수 있다면 조건문을 실행한다.
        if can_click:
            # 해당 채널은 가려고 하는 채널보다 작거나 같은 채널중 가장 큰 값이다.
            # 따라서 해당 채널의 길이와 n까지의 차이를 더한 값(n까지 +버튼을 눌러야 하는 값)을 result에 저장된 값과 비교해 더 작은 값을 넣어준다.
            result = min(result, len(str(i))+(n-i))
            break
    
    # n~99까지 n보다 크거나 같은 채널이 눌리는지 확인한다.
    # 100과의 차이는 기본값에 저장되었으므로 확인할 필요가 없다.
    for i in range(n, 100):
        # 위 코드와 거의 동일하다.
        can_click = True
        for button in buttons:
            if button in str(i):
                can_click = False
                break
        if can_click:
            # i가 n보다 크거나 같으므로 i와 n의 자리를 바꾼다.
            result = min(result, len(str(i))+(i-n))
            break

# 가려고 하는 채널이 100보다 큰 경우 조건문을 실행한다. 
else:
    # n~101까지 n보다 작거난 같은 채널을 확인한다.
    for i in range(n, 100, -1): 
        # 아래 코드는 위와 동일하다.
        can_click = True
        for button in buttons:
            if button in str(i):
                can_click = False
                break
        if can_click:
            result = min(result, len(str(i))+(n-i))
            break

    '''
    기본값을 생각해보자.
    우리는 n과 100의 차이를 기본값으로 가진다.
    즉, n - 100 보다 차이가 큰 값은 고려할 필요가 없다.
    따라서 n + n - 100까지 확인해 주면 된다(물론 자릿수를 빼줄 순 있지만 속도 상에 큰 문제는 없다.).
    '''
    for i in range(n, 2 * n - 100):
        # 아래 코드는 위와 동일하다.
        can_click = True
        for button in buttons:
            if button in str(i):
                can_click = False
                break
        if can_click:
            result = min(result, len(str(i))+(i-n))
            break

print(result)

# other solution(1348ms)
target = int(input())   # 채널을 입력받는다
ans = abs(100 - target) # 내 코드에서 result의 역할과 동일하며 result의 기본값과 동일하게 초기화한다.
M = int(input())        # 고장난 버튼 개수를 입력받는다.
if M: # 고장난 버튼이 있는 경우만 수행한다.
    broken = set(input().split())
else:
    broken = set()

# 0~1,000,000까지 모든 수를 탐색한다. (500,000가 최대)
# 내 코드는 경우마다 최적화하여 더 빠르다. 
for num in range(1000001): 
    # 아래 코드는 내 코드와 동일하다.
    for N in str(num):
        if N in broken:
            break
    else:
    	ans = min(ans, len(str(num)) + abs(num - target))

print(ans)