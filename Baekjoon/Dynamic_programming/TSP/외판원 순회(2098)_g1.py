import sys
input = sys.stdin.readline
INF = float("inf")

def dfs(now, before):                                           # now: 현재 방문한 도시, before: 현재까지 방문한 도시에 대한 정보가 담긴 변수
    if dp[now][before]: return dp[now][before]                  # 남아있는 경로를 이미 방문한적이 있다면 해당 값을 반환한다.
            
    if before == (1<<n) - 1:                                    # 모든 도시를 방문했다면 (1<<n)-1 값을 가진다(Ex) 도시가 5개라면 11111일 때 모든 도시를 방문한 것이다.) 
        return path[now][0] if path[now][0] > 0 else INF        # 모든 도시를 방문했다면 경로의 마지막 노드(현재 노드)가 출발 노드(0)과 이어져 있는지 확인한다.
      
    cost = INF
    for node in range(n):
        if before & (1<<node) == 0 and path[now][node] != 0:    # 해당 도시를 방문한 적이 없고, 현재 도시와 해당 도시간에 길이 있다면
            tmp = dfs(node, before | (1<<node))                 # before 변수에 이동할 도시의 방문 처리를 해주고 dfs에 전달한다.
            cost = min(cost, tmp + path[now][node])             # cost값을 갱신한다.(길이 있다면 최단 거리가 저장되고, 없다면 INF가 저장된다.)

    dp[now][before] = cost                                      # 갱신된 cost값을 dp[now][node]에 저장한다.
    return cost

n = int(input())                                                # 2 ≤ N ≤ 16
path = [list(map(int, input().split())) for _ in range(n)]      # 도시 사이의 길에 대한 정보를 담는 리스트
dp = [[0] * (1 << n) for _ in range(n)]                         # 메모이제이션에 이용할 리스트

print(dfs(0, 1<<0))                                             # 0에서부터 탐색을 수행하고 0번째 도시는 미리 방문처리를 해준다.                

'''
비트마스크를 통해 용량은 줄이고 속도는 증가시킬 수 있었다.
또한 dfs를 사용할 때 dp를 사용해 프로그램 성능을 향상 시킬 수 있다는 것도 좋은 아이디어 같다.
해당 내용은 꼭 알아두자.
'''