# My Solution(68ms)
from itertools import combinations
'''
로또 번호 k개 중에서 6개를 선택하면 된다.
즉, 조합을 구하는 것이랑 동일한 문제이므로 combinations 함수를 사용했다.
'''
while True:
    datas = list(map(int, input().split()))     # 데이터를 입력 받는다.

    if datas[0] == 0:                           # 입력된 데이터가 0이면 반복문을 종료한다.
        break

    k = datas[0]; s = list(map(str, datas[1:])) 

    for i in combinations(s, 6):                # 모든 조합의 경우를 구해 출력한다.
        '''
        (참고)
        sys.stdout.write(' '.join(i))를 사용해도 68ms가 나왔다.
        print(*i)의 경우 72ms가 나온다.
        '''
        print(' '.join(i))
    print()
