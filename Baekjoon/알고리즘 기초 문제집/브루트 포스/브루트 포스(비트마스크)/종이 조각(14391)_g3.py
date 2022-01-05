# My Solution(오답)
import sys
input = sys.stdin.readline

'''
단순히 세로 값들을 모두 더해주고, 가로 값들을 모두 더해줘서
더 큰 결과가 정답이라고 생각했지만 예외가 있었다.

반례:
0009
0109
0109
-> 999 + 10 + 10 = 1019
-> 내 코드는 999 + 11을 최대값으로 측정한다.
'''

n, m = map(int, input().split()) # 1 ≤ N, M ≤ 4
graph = [list(map(int, list(input().rstrip()))) for _ in range(n)]  # 모든 값을 입력받는 리스트다. 
graph_T = list(map(list, zip(*graph)))                              # 스타트와 링크 문제에서 배운 방법을 사용했다. 행(세로)방향을 계산할 때 사용할 것이다.

result1 = 0
for i in range(n):
    result1 += int(''.join(map(str, graph[i])))                     # 해당 행의 값들을 str로 변형해 문자열로 합치고 정수형으로 바꿔서 result1에 더한다.

result2 = 0
for i in range(m):
    result2 += int(''.join(map(str, graph_T[i])))                   # 위와 동일한 연산을 한다.

print(max(result1, result2))                                        # 더 큰 값을 비교해 큰 값을 출력한다.  

# Other Solution(1128ms)
'''
product 함수를 이용해 비트마스크 조합을 만들고 
0값을 가지는 위치들은 가로 방향으로 이동하고,
1값을 가지는 위치들은 세로 방향으로 이동시키며 계산했다.
직사각형이 차지하는 모든 경우를 살펴볼 수 있으므로 완전 탐색이 가능하다.
'''
import itertools

n, m = map(int, input().split())
x_lst = []
for _ in range(n):
    x_lst.append(list(map(int, (input()))))

# 1차원 리스트를 2차원 리스트로 변형해주는 함수다.
def to_matrix(l,m) :
    return [l[i:i+m] for i in range(0, len(l), m)]  # 열의 길이가 m이므로 step은 m으로 지정한다.

# itertools의 product를 이용해서 비트마스크 조합을 만든다.
# e.g) (0,0,0,0), (0,0,0,1) ... (1,1,1,1)
'''
product함수는 중복 순열을 뽑아주는 함수다. (permutations: 순열, combinations: 조합)
product(data, repeat = n) 식으로 사용하면 data에서 n개를 순서를 고려하고 중복을 허용해서 뽑아준다. 
'''
a = itertools.product([0, 1], repeat=n*m)
ans = 0

# 가로와 세로의 합계를 구해주고 더해줄 것이다.
for x in a:
    bit_mask = to_matrix(x, m)                      # 비트마스크 조합중 하나를 꺼내 x_lst와 동일한 형태로 만든다.
    sumh = 0                                        # 가로 방향의 직사각형 모형들의 합들을 저장할 변수다.

    for i in range(n):
        hori = 0                                    # 계산해 왔던 값들의 합을 임시 저장할 변수다.
        for j in range(m):      
            if bit_mask[i][j] == 0:                 # 0인 곳은 모두 가로 방향으로 이동할 것이다.
                hori = 10 * hori + x_lst[i][j]      # 이전에 계산했던 값은 10을 곱해주고 현재 위치의 값을 더해준다.
            if bit_mask[i][j] == 1 or j == m - 1:   # 1인 지역은 세로 방향으로 이동할 위치이므로 움직임을 중단한다. j가 m-1면 반복문이 끝나므로 종료전에 아래 코드를 실행해야한다.
                sumh = sumh + hori                  # 지금까지 계산한 값을 sumh에 저장한다.
                hori = 0                            # hori를 0으로 초기화해준다.

    sumv = 0                                        # 세로 방향의 직사각형 모형들의 합들을 저장할 변수다.

    for j in range(m):
        vert = 0                                    # 계산해 왔던 값들의 합을 임시 저장할 변수다.
        for i in range(n):                      
            if bit_mask[i][j] == 1:                 # 1인 곳은 모두 가로 방향으로 이동할 것이다.
                vert = 10 * vert + x_lst[i][j]      # 위와 동일한 연산을 수행한다.
            if bit_mask[i][j] == 0 or i == n - 1:   # 0인 지역이라면 움직임을 중단한다. i가 n-1이면 반복문이 끝나므로 종료전에 아래 코드를 실행해야한다.
                sumv = sumv + vert                  # 위와 동일한 연산을 수행한다.
                vert = 0

    sum_all = sumh + sumv                           # sumh와 sumv의 합이 해당 비트마스크의 결과가 된다.
    ans = max(ans, sum_all)                         # ans와 sum_all중 큰 값을 ans에 저장한다.

print(ans)                                          # ans를 출력한다.

# 출처: https://statssy.github.io/alg/2020/03/27/baekjoon_14391/

'''
그리디가 안될 것이라는 것을 깨닫고 완전탐색을 사용해보려고 했지만, 어떻게 해야할 지 감이 잡히지 않았다.
해답을 보고 비트마스크 조합을 itertools 라이브러리의 product함수로 만들 수 있다는 사실을 처음 알게 되었다.
그리고 비트마스크의 조합을 이용해 위와 같이 수행시킬 수 있다는 점이 인상깊었다.
덕분에 배운점이 많은 것 같다. 위와 같은 방식은 기억해놓도록 하자. 
'''
