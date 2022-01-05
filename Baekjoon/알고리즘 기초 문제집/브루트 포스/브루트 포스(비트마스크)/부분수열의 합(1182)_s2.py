# My Solution1(312ms)
import sys
input = sys.stdin.readline

'''
N이 최대 20개 밖에 되지 않아 완전탐색으로 풀 생각을 했다.
DFS로 풀까?라고도 생각했지만 아래처럼 배열을 사용하는 편이 코드 작성면에서 쉬워보여 배열을 이용하기로 했다.

내가 푼 방식은 다음과 같다.
1. 수열에서 i번째 숫자를 꺼낸다.
2. i-1번째 숫자까지 계산할 수 있는 모든 경우의 수들은 result 리스트에 저장된다.
   따라서 result의 모든 원소와 arr[i]를 더해 result의 원소로 추가한다.
3. 위 과정을 n번 수행한다.
4. result에 모든 결과가 저장되어 있으므로 m의 개수를 세어주면 된다.
'''

n, s = map(int, input().split())        # 1 ≤ N ≤ 20, |S| ≤ 1,000,000
arr = list(map(int, input().split()))   # 수열을 입력받는다.

result = [arr[0]]                       # 수열에서 첫 번째 값은 미리 저장해둔다.
for i in range(1, n):
    append_list = [arr[i]]              # arr[i]를 임시 저장 리스트에 담아둔다.
    for j in result:                
        append_list.append(j + arr[i])  # 임시 저장 리스트에 이전 계산 결과들과 arr[i]의 합을 저장한다. 
    result = result + append_list       # result에 임시 저장 리스트에 저장된 결과들을 추가한다.
print(result.count(s))

# My Solution2(416ms)
'''
아래 코드는 위 코드의 원리와 동일하다.
n이 최대 20이라도 20이라는 값을 가지면 result의 크기는 매우 커진다.
1 + 2 + 3 + 6 + ... 
으로 데이터가 증가하기 때문에 count()에서 많은 시간을 소모할 수 있다고 생각했다.
그래서 count변수를 추가해 이전 데이터에 arr[i]를 더하고 list에 추가하고 동시에
해당 값이 s와 동일한지 확인했다.
하지만 조건문이 너무 많이 반복되는 탓인지 비용은 오히려 많이 들어간 것 같다.
'''
import sys
input = sys.stdin.readline

n, s = map(int, input().split())        # 1 ≤ N ≤ 20, |S| ≤ 1,000,000
arr = list(map(int, input().split()))   # 수열을 입력받는다.

result = []
count = 0 
for i in range(0, n):
    append_list = []
    for j in result:
        append_list.append(j + arr[i])
        if j + arr[i] == s: count += 1
    append_list.append(arr[i])
    if arr[i] == s: count += 1
    result = result + append_list
print(count)

# Other Solution1(624ms)
'''
이전에 n과 m_1 문제를 풀때 배운 combinations함수를 사용하면 해당 문제를 쉽게 풀 수 있다.
하나의 리스트에서 모든 조합을 계산해야 하면, permutations, combinations를 사용하면 된다는 사실을 꼭 기억하자.
사용법은 다음과 같다.
1. list(permutations(list, 2)) (순열)
2. list(combinations(list, 2)) (조합)
두 코드 동일하게 list의 원소를 2개씩 묶어준다.
'''
import sys
from itertools import combinations

n,s = map(int,sys.stdin.readline().split())
a = list(map(int,sys.stdin.readline().split()))

count = 0

for i in range(1,n+1) :
    sub = list(combinations(a,i))
    for c in sub :
        if sum(c) == s :
            count +=1
                
print(count)