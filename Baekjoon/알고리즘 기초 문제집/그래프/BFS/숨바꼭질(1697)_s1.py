# My Solution(bfs, 156ms)
'''
처음 수빈이의 위치와 동생의 위치가 주어지고, 수빈이가 동생의 위치까지 가는데 걸리는 최소한의 시간을 알면 된다.
이때 수빈이의 위치를 n이라 할 때 이동할 수 있는 좌표는 n-1, n+1, 2*n 총 3개의 좌표로 이동할 수 있다.
이 과정을 bfs 탐색 과정을 이용해 풀면 해당 좌표까지 가는 최단 시간을 구할 수 있다.
'''
import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())                # 수빈이의 위치와 동생의 위치를 입력받는다.(0 ≤ n, m ≤ 100,000)
visited = [False for _ in range(100001)]        # 현재까지 방문한 좌표를 저장할 리스트다.(방문 처리 용도 및 방문한 좌표 저장용이다.)

def bfs(start):
    q = deque([start])                          # 큐를 생성하고 시작점을 넣어준다.
    visited[start] = 1                          # 시작점의 visited값을 1로 초기화한다.

    while q:
        now = q.popleft()                       # 큐의 원소를 꺼낸다.

        if now == m:                            # 원하는 위치에 도달했다면
            return visited[now]-1               # 해당 위치의 visited값에 1을 뺀 값을 반환하고 함수를 종료한다.

        for i in (now-1, now+1, 2*now):         # 이동 가능한 좌표를 모두 탐색한다.
            if i < 0 or i > 100000:             # 인덱스 범위를 넘어가면 반복문으로 돌아간다.
                continue

            if not visited[i]:                  # 해당 좌표를 방문한 적이 없다면
                q.append(i)                     # 큐에 추가하고, 현재 좌표의 visited값에 1을 더한 값을 저장한다.
                visited[i] = visited[now]+1

print(bfs(n))