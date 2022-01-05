# My Solution(3880ms)
import sys
input = sys.stdin.readline
'''
비어있는 공집합 S가 주어졌을 때, 아래 연산을 수행하도록 해야한다.

1. add x: S에 x를 추가한다. (1 ≤ x ≤ 20) S에 x가 이미 있는 경우에는 연산을 무시한다.
2. remove x: S에서 x를 제거한다. (1 ≤ x ≤ 20) S에 x가 없는 경우에는 연산을 무시한다.
3. check x: S에 x가 있으면 1을, 없으면 0을 출력한다. (1 ≤ x ≤ 20)
4. toggle x: S에 x가 있으면 x를 제거하고, 없으면 x를 추가한다. (1 ≤ x ≤ 20)
5. all: S를 {1, 2, ..., 20} 으로 바꾼다.
6. empty: S를 공집합으로 바꾼다.

위 명령들을 보면 집합의 원소는 1~20까지 밖에 있을 수 없다.
그래서 각 원소가 집합에 있다면 1, 없으면 0을 원소로 가지는 리스트 s를 만들고
명령을 입력받아 수행하는 방식으로 코드를 작성했다.

'''
s = [0 for _ in range(21)]                          # 1~20까지 해당 원소가 있는지 없는지를 표시하기 위해 리스트를 생성했다.

for _ in range(int(input())):
    a= input().rstrip().split()                     # 명령을 입력받는다.
                                                    # 이후 각 명령에 맞게 수행한다.
    if a[0] == 'all':                           
        s = [0] + [1 for _ in range(20)]
        continue    
    elif a[0] == 'empty':
        s = [0 for _ in range(21)]
        continue

    b = int(a[1])
    if a[0] == 'add':
        if not s[b]: s[b] = 1
    elif a[0] == 'remove':
        s[b] = 0
    elif a[0] == 'check':
        if s[b] == 1: print(1)
        else: print(0)
    elif a[0] == 'toggle':
        if s[b] == 1: s[b] = 0
        else: s[b] = 1

'''
다른 사이트를 찾아봤는데 다들 집합 자료형을 이용해 풀었다.
돌려보니 시간은 내 코드가 더 절약되는 것같다.
비트마스크를 약간 응용하는 방식도 매우 좋은 풀이법이 되는 듯 하다.
''' 

