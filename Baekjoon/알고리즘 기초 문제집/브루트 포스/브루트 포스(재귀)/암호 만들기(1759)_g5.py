# My Solution1(84ms)
'''
백트래킹을 사용한 방법이다.
dfs함수를 구현해 모든 경우를 확인하도록 코드를 작성했다.
'''
import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

a, b = map(int, input().split())
arr = input().split()
arr.sort()                                          # 사전 순으로 탐색해야 하므로 입력받은 알파벳을 정렬한다.                

def dfs(now, count, result):
    if count == a:                                  # a개의 알파벳을 골랐는지 확인한다.
        check = 0
        for i in ['a', 'e', 'i', 'o', 'u']:         # 모음의 개수를 센다.
            if i in result: check += 1

        if check >= 1 and len(result)-check >= 2:   # 모음이 1개 이상이고 자음이 2개 이상인지 확인한다.
            print(''.join(result))
        return

    for i in range(now+1, b):                       # 사전순으로 출력되어야 하므로 now+1~b까지의 알파벳을 뽑는다.
        dfs(i, count+1, result+[arr[i]])            # 해당 알파벳을 result에 넣고 dfs를 수행한다. 

for i in range(0, b-a+1):                             # range(0, b) -> 84ms / range(0, b-a+1) -> 76ms                            
    dfs(i, 1, [arr[i]])

# My Solution2(68ms)
'''
combinations를 활용해 모든 조합의 경우를 확인한 방법이다.
이전에 순열 및 조합 문제를 풀면서 느꼈지만 수열 및 조합 문제는 대부분 dfs로도 풀리는 것 같다.
'''
from itertools import combinations
a, b = map(int, input().split())
arr = input().split()
arr.sort()

for i in combinations(arr, a):
    check = 0

    for j in ['a', 'e', 'i', 'o', 'u']:             # 모음의 개수를 센다.
        if j in i: check += 1

    if check >= 1 and len(i)-check >= 2:            # 모음이 1개 이상이고 자음이 2개 이상인지 확인한다.
        print(''.join(i))
        
