import sys
input = sys.stdin.readline

'''
PS: '(', ')'로만 구성된 문자열
VPS: PS 중 괄호의 모양이 바르게 구성된 문자열
'''

# My Solution(68ms)
'''
문자열 안에 '()'가 있으면 계속 제거하는 방식을 사용함.
VPS인 임의의 x가 있다면 (x)는 무조건 VPS임.
따라서 가장 안쪽의 ()부터 계속 지울 때, 마지막까지 가서도 괄호가 남는다면, 해당 PS는 VPS가 아님.
'''
for _ in range(int(input())):
    string = input().rstrip()
    
    while '()' in string:
        string = string.replace('()', '')
    
    if string == '': 
        print('YES')
    else: 
        print('NO')
        
# Other Solution(68ms)
'''
'('가 나올 때는 +1, ')'가 나올 때는 -1을 해준다 가정하자.
만약 짝이 맞는다면 총 결과는 0이 되어야 한다.
단, 양수인 경우 끝까지 진행해야 하지만, 음수가 된 순간부터 해당 PS는 VPS가 될 수 없다는 사실을 주의해야 한다.
'''
for _ in range(int(input())):
    string = input().rstrip()
    
    result = 0
    for i in string:
        if i == '(':
            result += 1
        else: 
            result -= 1
            if result < 0: break
    
    if result == 0: 
        print('YES')
    else: 
        print('NO')