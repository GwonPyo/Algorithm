# My Solution(3036ms)
import sys
from itertools import combinations
input = sys.stdin.readline
'''
단순히 combinations 함수만을 사용해 풀었다.
처음에는 해당 인원들을 n//2명씩 뽑아 조합을 만들었다.
이때 combinations 함수의 특성을 이용해 team1과 team2를 뽑아줬다.
예를 들어, combinations 함수로 만들어진 리스트에서 0번째 리스트와 -1번째 리스트는 서로 여집합 관계에 있다.
team1와 team2 만들고 각 팀마다 2명씩 뽑아 조합을 한 번 더 만들어 줬다.
그리고 해당 조합을 이용해 team1과 team2의 차이를 일일이 구해줬다.
'''
n = int(input())                                                # 총 인원의 수이다.
people = list(range(n))                                         # 인원의 수 만큼 원소를 만들어준다.
graph = [list(map(int, input().split())) for _ in range(n)]     # 각 사람들이 팀이 되었을 때 얻는 점수가 저장된 리스트다.

team = list(combinations(people, n//2))                         # combinations로 팀을 나눠준다.

result = int(1e9)                                               # 결과를 저장할 변수다.
for i in range(len(team)//2):                                   # (조합의 개수)//2번만 수행하면 된다.
    team1 = team[i]                                             # team1을 선택한다.
    team2 = team[-(i+1)]                                        # team2를 선택한다.
    team1_cb = list(combinations(team1, 2))                     # team1에서 2명씩 뽑아 조합을 만든다.
    team2_cb = list(combinations(team2, 2))                     # team2에서 2명씩 뽑아 조합을 만든다.

    count = 0                                                   # 해당 팀들로 구성된 경우 두 팀의 차이를 저장할 변수다.
    for j in range(len(team1_cb)):                              
        a, b = team1_cb[j]                                      
        count += (graph[a][b] + graph[b][a])                    # team1에서 나오는 점수는 모두 더해준다.

        a, b = team2_cb[j]
        count -= (graph[a][b] + graph[b][a])                    # team2에서 나오는 점수는 모두 빼준다.

    result = min(result, abs(count))                            # result와 count의 절대값을 비교해 더 큰 값을 result에 저장한다.

print(result)                                                   # result를 출력한다.


# Other Solution1(120ms)
import sys
from itertools import combinations as cb
N = int(sys.stdin.readline()) // 2
M = 2*N                                                                     # 총 인원 수이다.
stat = [list(map(int, sys.stdin.readline().split())) for _ in range(M)]     # 내 코드에서 graph와 동일한 리스트다.


'''
zip(*stat)를 사용하면 해당 리스트를 transpose시킬 수 있다.
즉, 각 행을 zip한다는 의미이므로 열이 행으로 가고 행은 열로 가는 효과를 낼 수 있다.
꼭 기억해두자.
'''

newstat = [sum(i) + sum(j) for i, j in zip(stat, zip(*stat))]               # 각 인원들이 팀이 되었을 때 얻는 점수들을 모두 더해 저장한다. (1번째 사람은 1열과 1행의 값들을 모두 더한다.)       
allstat = sum(newstat) // 2                                                 # newstat의 모든 값을 더하면 stat의 모든 원소를 두 번씩 더한 것과 같다. 따라서 2로 나눠준다.

mins = 65535
for l in cb(newstat[:-1], N):                                               # 1~n-1 사람 중 n//2 명을 뽑는다.
    mins = min(mins, abs(allstat - sum(l)))                                 # 해당 사람들의 값은 allstat에 빼준다. 그러면 해당 연산에 관련이 없는 값들은 모두 빼지고 team2는 한 번 더 빼지는 효과가 있으므로 올바른 결과가 나온다.
print(mins)
