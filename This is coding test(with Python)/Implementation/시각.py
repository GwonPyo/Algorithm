# 2021.11.04 코드
# 이전 코드와 원리는 동일하고 코드가 더 깔끔해서 교체함.
'''
총, 분에 3이 포함된 개수
3, 13, 23, 43, 54 / 5개
30~39 / 10개
총 15개

시에 3이 포함된 개수
3, 13, 23 
총 3개

시가 3이 아닐 때 개수: 60 * 60 - (3이 들어 있지 않은 초, 분의 조합) = 60 * 60 - (45 * 45)
시가 3일때 개수: 60 * 60
'''

n = int(input()) # 시(00시 00분 00초 ~ n시 59분 59초)

hour_not_3 = 60 * 60 - (45 * 45)
hour_3 = 60 * 60

if n >= 23:
    print(hour_not_3 * (n - 2) + hour_3 * 3)
elif n >= 13:
    print(hour_not_3 * (n - 1) + hour_3 * 2)
elif n >= 3:
    print(hour_not_3 * (n) + hour_3 * 1)
else:
    print(hour_not_3 * (n + 1))

# 책 풀이
'''
책의 코드는 완전 탐색으로 풀었다.
내 코드는 O(1)시간으로 시간을 훨씬 적지만 책의 코드도 분석해보자.

사실 00시 00분 00초 ~ 23시 59분 59초 까지의 모든 경우의 수는 
24 * 60 * 60 = 86,400 밖에 되지 않는다.
따라서 완전 탐색으로 풀어도 아무 문제가 없다.
코드의 가독성으로는 아래 코드가 좋은 것 같다.
'''

n = int(input())

count = 0
for hour in range(n + 1):
    for minute in range(60):
        for second in range(60):
            if '3' in str(hour) + str(minute) + str(second):
                count += 1

print(count)