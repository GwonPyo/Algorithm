# My Solution(744ms)
import sys
input = sys.stdin.readline

'''
문제를 보자마자 dfs로 풀어야겠다는 생각을 했다..
우선 n의 최대값은 10이다.
즉, 모든 노드가 완전히 이어져 있는 경우라도, 2 * 10! = 7257600로 1초 이내에 수행이 가능하다.
'''

n = int(input())                                            # 2 ≤ N ≤ 10
visited = [False for _ in range(n)]                         # 방문 여부를 확인할 리스트다.
graph = [list(map(int, input().split())) for _ in range(n)] # graph를 입력받는다.(이동 값을 입력받는다.)
result = int(1e9)                                           

def dfs(now, path, count):
    global result
    if count == n and graph[now][0] > 0:                    # 모든 노드를 방문했고, 마지막 노드와 1(출발점)이 이어져 있다면
        result = min(result, path + graph[now][0])          # 현재 result와 비교해서 최소 비용을 result에 저장한다.
        return
    for i in range(n):                                      # 모든 노드를 방문하지 못했다면
        if not visited[i]:                                  # 지금까지 방문하지 않은 노드를 확인한다.
            if graph[now][i] > 0:                           # 방문하지 않은 노드와 현재 노드가 연결되어 있다면 
                visited[i] = True                           # 방문 처리를 한다.
                dfs(i, path+graph[now][i], count+1)         # 다음 위치로 이동해 dfs를 수행한다.
                visited[i] = False                          # 미방문 처리를 한다.

visited[0] = True
dfs(0, 0, 1)
print(result)