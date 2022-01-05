# 2021.11.07
# My solution
# 1 ≤ E ≤ 15, 1 ≤ S ≤ 28, 1 ≤ M ≤ 19
E, S, M = map(int, input().split())

'''
E, S, M을 각각 15, 28, 19의 나머지로 표현해야 하는데
15, 28, 19는 나머지로 표현이 불가능하다. 
따라서 해당 값들은 연산 이전에 미리 0(나머지)으로 바꾼다.
'''

if E == 15: E = 0
if S == 28: S = 0
if M == 19: M = 0

'''
모두 0인 경우 가장 빠른 해는 당연히 0년으로 출력된다.
하지만 0년은 없다. 따라서 count를 미리 1로 늘려서 연산을 수행한다.
'''
count = 1 if E == 0 and S == 0 and M == 0 else 0
while True:
    # 한번 반복할 때 3개의 수를 비교한다.
    e = 15 * count + E
    s = 28 * count + S
    m = 19 * count + M
    if S == e % 28 and M == e % 19:
        print(e)
        break
    elif E == s % 15 and M == s % 19:
        print(s)
        break 
    elif E == m % 15 and S == m % 28:
        print(m)
        break   
    count += 1

# Other solution
E, S, M = map(int, input().split())

'''
값들을 미리 0으로 바꾸는 이유는 위의 코드랑 동일하다.
하지만 해당 코드는 result = S로 미리 설정했다.
생각해보면 간단하다.
S에 29를 계속 더하면, 결국 가장 빠른 연도에 가장 빠르게 도달할 것이다.
왜냐하면 E에 15를 계속 더하든, M에 19를 계속 더하든 결국에는 도달하는 같은 연도를 찾는 것이 목표이다.
따라서 S를 기준으로 생각하면 가장 빠르게 결론에 도달할 수 있다.
이때 S = 28일 경우를 대비해 result에 먼저 S를 넣어주는 것을 볼 수 있다.
'''

result = S
if E == 15: E = 0
if S == 28: S = 0
if M == 19: M = 0
# result값이 맞는지 확인하고, 아닌 경우 28을 더한다.
while True:
	if result%15 == E and result%28 == S and result%19 == M:
		break
	result += 28
print(result)