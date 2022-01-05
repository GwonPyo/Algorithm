# My Solution(180ms)

'''
dfs를 활용해 풀었다.
숫자 0~9까지 모든 숫자를 탐색하는 방식이다.
처음에 0을 첫번째 자리에 넣어보고, 다음에는 1을 탐색하고 부등호를 만족하면 
2를 탐색하고 부등호를 만족하지 않으면 다시 돌아가서 3을 탐색하고 ...
이런 식으로 탐색을 수행한다.
'''

import sys
input = sys.stdin.readline

k = int(input())                        # 부등호의 개수를 입력받는다.(2 ≤ k ≤ 9)
data = list(input().split())            # 부등호를 입력받는다.
visited = [False for _ in range(10)]    # 방문 여부를 확인해줄 리스트다.
result = []                             # 탐색중 임시로 저장할 결과다.
results = []                            # 탐색이 완료된 리스트(result)를 저장할 리스트다.
def dfs(now, count):                    
    if count == k:                                  # 부등호 개수 + 1개의 숫자를 탐색했다면
        results.append(''.join(map(str, result)))   # 해당 결과를 문자열로 results에 저장한다.
        return
        
    for i in range(10):                                                                 # 0~9까지 탐색한다.
        if not visited[i]:                                                              # 해당 숫자를 방문하지 않았고,
            if (data[count] == '>' and now > i) or (data[count] == '<' and  now < i):   # 부등호를 만족한다면
                visited[i] = True       # 해당 숫자를 방문 처리한다.
                result.append(i)        # result에 추가한다.
                dfs(i, count+1)         # dfs를 수행한다.
                visited[i] = False      # 해당 숫자에 대한 dfs가 끝나면 미방문 처리한다.
                result.pop()            # result에서 해당 숫자를 빼준다.

for i in range(10):                     # 0~9까지 탐색한다.
    visited[i] = True                   # dfs의 과정과 동일하게 탐색한다.
    result.append(i)
    dfs(i, 0)
    visited[i] = False
    result.pop()

print(results[-1])                      # 가장 마지막에 나온 결과가 최대 정수가 된다.
print(results[0])                       # 가장 처음에 나온 결과가 최소 정수가 된다.

# Other Solution()
n = int(input())                        # 부등호 개수를 입력받는다.
op = input().split()                    # 부등호를 입력받는다.
c = [False] * 10                        # 방문여부 확인을 위한 리스트다.
mx, mn = "", ""                         # 가장 큰 정수를 저장할 mx, 가장 작은 정수를 저장할 ms 변수이다.

def possible(i, j, k):                  # 해당 부등호를 만족하는지 확인해주는 함수다.
    if k == '<':
        return i < j
    if k == '>':
        return i > j
    return True

def solve(cnt, s):                                              # 완전 탐색을 수행하는 함수다(dfs)
    global mx, mn
    if cnt == n + 1:                                            # cnt가 모든 수를 탐색했다면(부등호 개수에 맞는 최대 개수만큼 탐색했다면)
        if not len(mn):                                         # mn에 저장된 결과가 없다면
            mn = s                                              # mn에 저장한다.
        else:                                                   # mn에 저장된 결과가 있다면
            mx = s                                              # mx에 저장한다.
        return
    for i in range(10):                                         # 0~9까지 탐색한다.
        if not c[i]:                                            # 해당 숫자를 방문하지 않았고
            if cnt == 0 or possible(s[-1], str(i), op[cnt - 1]):# 부등호 조건에 맞거나 cnt가 0(cnt가 0일 땐, 비교할 수가 없기 때문이다.)이라면
                c[i] = True                                     # 방문 처리한다.
                solve(cnt + 1, s + str(i))                      # 해당 숫자를 넣어주고 solve()함수를 수행한다.
                c[i] = False                                    # solve함수의 동작이 끝나면 다시 미방문 처리한다.
solve(0, "")
print(mx)
print(mn)

