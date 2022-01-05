# my solution(1412ms)
import sys
input = sys.stdin.readline

# n: 종이의 세로 길이, m: 종이의 가로 길이
# 4 <= n, m <= 500
n, m = map(int, input().split())
# 종이를 생성한다.
arr = []
# 종이의 각 칸에 숫자를 입력받는다. (숫자는 1,000을 넘지 않는 자연수다.)
for _ in range(n):
    arr.append(list(map(int, input().split())))

'''
완전 탐색으로 풀어야 한다고 생각했다.
그리디로 풀기에는 불가능해 보였고 그렇다고 dp를 사용하기에도 무리가 있었다.
더군다다 크기가 4 ~ 500이므로 완전 탐색을 해도 
(일직선) -> 1개 * ((n * (m-3)) + ((n-3) * m))       O(2nm)
(정사각형) -> 1개 * ((n-1) * (m-1))                 O(nm)
(나머지) -> 3개 * ((n-1) * (m-2) + (n-2) * (m-1))   O(6mn)
으로 많아도 8 * 500 * 500 = 2,000,000 밖에 걸리지 않는다.
'''

# 일직선 형태를 확인하는 함수다.
def pattern1():
    '''
    해당 도형을 arr위에서 움직이며 계속 값을 확인해 줄 것이다.
    단 두 가지 형태를 확인해야 한다.
    1. ■
       ■
       ■
       ■ (수직)
    2. ■■■■ (수평)
    하면서 result와 비교해 더 크면 result 값을 해당 값으로 변경해야 한다.
    '''
    result = -1
    
    # 먼저 수직으로 탐색해 보자. 
    for x in range(0, n - 3):
        for y in range(0, m):
            # 모든 값을 더해서 result와 비교해본다.
            # 더 크다면 result에 값을 대입한다.
            result = max(result, arr[x][y] + arr[x+1][y] + arr[x+2][y] + arr[x+3][y])
    
    # 수평일 때를 탐색해본다. 이하 과정은 수평일 때와 동일하다.
    for x in range(0, n):
        for y in range(0, m - 3):
            result = max(result, sum(arr[x][y:y+4]))
    
    return result

# 정사각형 형태를 확인하는 함수다.
def pattern2():
    '''
    정사각형은 회전해도 모양이 똑같다.
    ■■
    ■■
    따라서 그냥 위아래, 양옆으로 이동시키며 값을 확인하면 된다.
    '''
    result = -1
    for x in range(0, n-1):
        for y in range(0, m-1):
            result = max(result, arr[x][y] + arr[x+1][y] + arr[x][y+1] + arr[x+1][y+1])
    return result

# 나머지 도형을 확인해보자(3개)
def pattern3():
    result = -1
    '''
    나머지 도형을 생각해보면 
    ■■■
    ■■■
    위 도형안에 들어간다.
    따라서 위 도형을 위아래, 양옆으로 이동시키면서 값의 위치에 알맞게 더하고
    모든 값을 비교해 가장 큰 값을 result에 대입한다.
    물론
    ■■
    ■■
    ■■
    의 경우도 비교해야 하므로 반복문을 두 개 써줬다. 
    '''
    for x in range(0, n-1):
        for y in range(0, m-2):
            # 6칸을 모두 더 해주고(six_num에 저장) 포함되지 않는 칸을 빼줬다. 
            six_sum = sum(arr[x][y:y+3]) + sum(arr[x+1][y:y+3])
            result = max(result, six_sum - arr[x][y] - arr[x][y+1],
            six_sum - arr[x][y+1] - arr[x][y+2],
            six_sum - arr[x+1][y] - arr[x+1][y+1],
            six_sum - arr[x+1][y+1] - arr[x+1][y+2],
            six_sum - arr[x][y] - arr[x][y+2],
            six_sum - arr[x+1][y] - arr[x+1][y+2],
            six_sum - arr[x][y+2] - arr[x+1][y],
            six_sum - arr[x+1][y+2] - arr[x][y])
    
    for x in range(0, n-2):
        for y in range(0, m-1):
            six_sum = sum(arr[x][y:y+2]) + sum(arr[x+1][y:y+2]) + sum(arr[x+2][y:y+2])
            result = max(result, six_sum - arr[x][y] - arr[x+1][y],
            six_sum - arr[x][y+1] - arr[x+1][y+1],
            six_sum - arr[x+1][y] - arr[x+2][y],
            six_sum - arr[x+1][y+1] - arr[x+2][y+1],
            six_sum - arr[x][y] - arr[x+2][y],
            six_sum - arr[x][y+1] - arr[x+2][y+1],
            six_sum - arr[x][y] - arr[x+2][y+1],
            six_sum - arr[x+2][y] - arr[x][y+1])
    
    return result

# 위 함수들을 수행시킨다.
# 그리고 반환된 값중 가장 큰 값을 출력한다.
result = max(pattern1(), pattern2(), pattern3())
print(result)

# Other solution(228ms)
def dfs(r, c, idx, total):
    global ans
    # 현재까지 점검한 칸의 합(total)과 
    # (2차원 배열에서 가장 큰 값)max_val을 탐색할 수 있는 남은 칸 만큼 곱한 값을 더했을 때
    # ans(현재까지 최대합)보다 작거나 같으면 가지치기를 실시한다.(유망하지 않음)
    if ans >= total + max_val * (3 - idx):
        return
    # 만약 총 4번을 검색했다면 ans와 total을 비교해본다.
    if idx == 3:
        ans = max(ans, total)
        return
    else:
        # 모든 칸으로 이동해본다.
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            # 종이칸(2차원 배열)의 범위를 넘지 않았고 방문한 위치가 아니라면 조건문을 실행한다.
            if 0 <= nr < N and 0 <= nc < M and visit[nr][nc] == 0:
                # 지금까지 총 2칸을 탐색했다면 아래 조건문을 실행한다.
                if idx == 1:
                    '''
                    dfs를 이용해 단순히 4칸을 탐색할 때는 아래와 같은 모양들을 탐색할 수 있다.
                    1. ■■■■ 2. ■■ 3.■■  4. ■■■
                               ■■    ■■      ■
                    모양이 회전되어도 탐색이 가능하다.
                    
                    하지만 
                     ■
                    ■■■
                    모양을 찾지 못한다.
                    해당 모양을 찾기 위해서는 현재 위치에서 이동하지 않고, 한번더 이동할 곳을 찾으면 된다.
                    아래코드로 해당 동작을 수행할 수 있다.
                    '''
                    visit[nr][nc] = 1                       # 이동할 위치인 nr, nc에 방문 처리를 한다.
                    dfs(r, c, idx + 1, total + arr[nr][nc]) # 현재 위치에서 다시 한 번 탐색한다.
                    visit[nr][nc] = 0                       # 이동한 위치인 nr, nc를 다시 미방문 처리한다.
                visit[nr][nc] = 1                           # 이동할 위치인 nr, nc에 방문 처리를 한다.
                dfs(nr, nc, idx + 1, total + arr[nr][nc])   # 이동할 위치로 이동하고 남은 dfs를 수행한다.
                visit[nr][nc] = 0                           # 이동한 위치인 nr, nc를 다시 미방문 처리한다. 

N, M = map(int, input().split())                            # n, m(종이 크기)을 입력받는다.
arr = [list(map(int, input().split())) for _ in range(N)]   # 세로 길이인 n만큼 행을 입력받는다.
visit = [([0] * M) for _ in range(N)]                       # 방문 여부를 체크하기 위한 리스트를 만든다. 
dr = [-1, 0, 1, 0]                                          # u, r, d, l 이동시 변경되는 row
dc = [0, 1, 0, -1]                                          # u, r, d, l 이동시 변경되는 col 
ans = 0                                                     # 지금까지 가장 컸던 합(answer)
max_val = max(map(max, arr))                                # 2차원 배열에서 가장 큰 값을 저장한다.

for r in range(N):
    for c in range(M):
        '''
        * 백트래킹
        해를 찾아가는 도중, 지금의 경로가 해가 될 것 같지 않으면 그 경로를 더이상 가지 않고 되돌아간다.
        즉, 코딩에서는 반복문의 횟수를 줄일 수 있으므로 효율적이다.
        이를 가지치기라고 하는데 불필요한 부분을 쳐내고 최대한 올바른 쪽으로 간다는 의미이다.
        
        정리하자면 백트래킹은 모든 가능한 경우의 수 중에서 특정한 조건을 만족하는 경우만 살펴보는 것이다.
        즉, 답이 될 만한지 판단하고 그렇지 않으면 그 부분까지 탐색하는 것을 하지 않고 가지치기 하는 것을 백트래킹이라고 생각하면 된다.
        '''
        visit[r][c] = 1         # r, c를 방문 처리한다.
        dfs(r, c, 0, arr[r][c]) # dfs를 수행한다.
        visit[r][c] = 0         # r, c를 다시 미방문 처리한다.

print(ans)