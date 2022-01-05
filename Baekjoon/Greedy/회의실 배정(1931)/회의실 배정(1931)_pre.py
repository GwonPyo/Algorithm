# 이전에 사용한 풀이이다.
# 시간은 4408ms로 2021.11.03 풀이(328ms)보다 느리다.
# 어디서 시간이 늦춰지는지 분석해보자.

n = int(input())
s = []

for i in range(n):
    first, second = map(int, input().split())
    s.append([first, second])
s = sorted(s, key=lambda a: a[0])
s = sorted(s, key=lambda a: a[1])

# 이 코드에서 last는 현재 회의의 종료시간을 저장한다.
last = 0
# cnt는 result와 동일한 역할이다.
cnt = 0
# 이 코드에서는 반복문을 s의 원소로 수행하고 있다.
# 이런 방법도 고려하면 편할 뜻하다.
for i, j in s:
    # 2021.11.03 코드와 동일하게 현재 회의의 종료시간과 시작시간을 비교한다.
    if i >= last:
        # 조건을 만족하면 cnt(result)의 값에 1을 더해주고
        # last 값을 j(다음 회의 종료값)로 바꿔준다.
        cnt += 1
        last = j
print(cnt)

'''
전체적인 풀이 방법은 2021.11.03 코드와 동일하다.
sys.stdin.readline() 대신 input()을 사용해 시간이 늦춰졌다고 생각한다. 
2021.11.03 코드처럼 start, end가 아닌 last하나로 해결하는 방법,
반복문을 index가 아닌 배열의 원소로 반복하는 방법은 괜찮은 듯 하다.
'''