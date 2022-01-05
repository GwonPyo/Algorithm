# My solution(2776)
import sys
input = sys.stdin.readline

# 테스트케이스 만큼 반복한다.
for _ in range(int(input())):
    # 1 <= m, n <= 40,000, 1 <= x <= m, 1 <= y <= n
    m, n, x, y = map(int, input().split())

    '''
    x와 y는 연도를 m과 n으로 나눴을 때의 나머지라고 생각해야 한다.
    하지만 x가 m이거나 y가 n이면 그럴 수가 없다.
    따라서 x가 m이면 0, y가 n이면 0으로 바꿔야 한다.
    '날짜 계산(1476)'에서도 동일한 과정을 사용했다.
    '''
    if x == m: x = 0
    if y == n: y = 0
    
    '''
    연도가 될 수 있는 최대값은 m과 n의 최대공약수다.
    최소공배수 알고리즘은 잘 몰라 반복문을 사용해 구현했다.
    '''
    # m과 n중 큰 값을 고른다.
    lcm = max(m, n)
    
    # 큰 값이 m이라면 아래 코드를 실행한다.
    if lcm == m:
        # lcm이 n의 배수라면 코드를 종료한다.
        while lcm % n != 0:
            # lcm이 n의 배수가 아니면 m을 더한다.
            lcm += m
    # 큰 값이 n이라면 아래 코드를 실행한다.
    # 위 코드와 동일하다.
    else:
        while lcm % m != 0:
            lcm += n

    '''
    이후에는
    날짜 계산에서 사용한 방식을 그대로 이용했다.
    만약 m이 더 크다면, x에 m을 계속 더하고 해당 값을 n으로 나눴을 때 y가 나오면 해당 값이 연도다.
    n이 더 클때도 동일한 방식으로 진행하면 된다.
    '''
    if max(m, n) == m:
        # x가 0인 경우는 존재하지 않는다.
        # 그리고 x가 0일 때 해당 값을 그대로 사용하면 y도 0일 때 연도가 0이 된다.
        # 따라서 x가 0인 경우 원래 값인 m을 더 해준다.
        # 날짜 계산(1476)방식을 사용해도 상관없다.
        if x == 0: x += m
        # x가 최소공배수 보다 크다면 반복문을 종료한다.
        while x <= lcm:
            # x를 n으로 나눴을 때의 나머지가 y라면 x가 연도가 된다.
            if x % n == y:
                # x를 출력한다.
                print(x)
                break
            # x가 연도가 아니라면 m을 더한다.
            x += m
        if x > lcm:
            print(-1)
    # 위 코드와 동일하다.
    else:
        if y == 0: y += n
        while y <= lcm:
            if y % m == x:
                print(y)
                break
            y += n
        if y > lcm:
            print(-1)

# My solution2(using_math.lcm, 1436ms)

import math

for _ in range(int(input())):
    # 1 <= m, n <= 40,000, 1 <= x <= m, 1 <= y <= n
    m, n, x, y = map(int, input().split())

    if x == m: x = 0
    if y == n: y = 0

    LCM = math.lcm(m, n)

    if max(m, n) == m:
        if x == 0: x += m
        while x <= LCM:
            if x % n == y:
                print(x)
                break
            x += m
        if x > LCM:
            print(-1)
    else:
        if y == 0: y += n
        while y <= LCM:
            if y % m == x:
                print(y)
                break
            y += n
        if y > LCM:
            print(-1)

# Other Solution(2232ms)
def num(m, n, x, y):
    # m, n을 곱한 값보다 작은 값인 경우에만 반복한다.
    # 최소공배수까지만 해도 되지만 최소공배수까지 계산하면 시간초과가 발생한다.
    while x <= m * n:
        # x-y가 n의 배수라면 x를 반환한다.
        if (x - y) % n == 0:
            return x
        # x에 m을 더한다.
        x += m
    # 연도를 구할 수 없으므로 -1을 반환한다.
    return -1

t = int(input())
for i in range(t):
    m, n, x, y = map(int, input().split())
    print(num(m, n, x, y))