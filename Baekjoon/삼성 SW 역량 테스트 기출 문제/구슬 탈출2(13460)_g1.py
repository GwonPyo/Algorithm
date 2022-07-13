import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())                                                    # 행과 열을 받아온다.
board = [list(input().rstrip()) for _ in range(n)]                                  # 보드판을 받아온다.
dx = (-1, 1, 0, 0)                                                                  # 이동 방향에 따른 좌표 이동을 담은 튜플을 선언한다.
dy = (0, 0, -1, 1)  

visited = [[[[False] * m for _ in range(n)] for _ in range(m)] for _ in range(n)]   # 방문여부를 visited[red_x좌표][red_y좌표][blue_x좌표][blue_y좌표]로 체크한다.

def move(x, y, dx, dy):
    cnt = 0                                                                         # 이동 칸 수를 저장할 변수다.
    
    while board[x+dx][y+dy] != '#' and board[x][y] != 'O':                          # 다음 칸이 벽이거나 현재 위치가 구멍이면 이동을 멈춘다.
        x += dx                                                                     # 좌표를 이동시킨다.
        y += dy
        cnt += 1
    return x, y, cnt                                                                

rx, ry, bx, by = 0, 0, 0, 0                                                         # 빨간 공과 파란 공의 좌표를 저장할 변수를 선언한다.
for i in range(n):
    for j in range(m):
        if board[i][j] == 'R':
            rx, ry = i, j
        elif board[i][j] == 'B':
            bx, by = i, j
            
queue = deque([])
queue.append((rx, ry, bx, by, 0))
visited[rx][ry][bx][by] = True

result = False    
while queue: 
    rx, ry, bx, by, depth = queue.popleft()
    if depth > 10:                                                                  # 이동 횟수가 10번을 넘어가면 반복문을 종료한다.
        break
    
    if board[bx][by] != 'O':                                                        # 파란공이 구멍에 들어가지 않고
        if board[rx][ry] == 'O':                                                    # 빨간공이 구멍에 들어갔다면
            result = True                                                           # result를 갱신해주고 총 횟수를 출력한다.
            print(depth)                                                            
            break
    
    for i in range(4):                                                              # 4방향 이동을 시도한다.
        nrx, nry, rcnt = move(rx, ry, dx[i], dy[i])                                 # 이동시 빨간공의 좌표와 이동 횟수를 받아온다.
        nbx, nby, bcnt = move(bx, by, dx[i], dy[i])                                 # 이동시 파란공의 좌표와 이동 횟수를 받아온다.
        if board[nbx][nby] != 'O':                                                  # 파란공이 구멍에 들어가지 않고
            if nrx == nbx and nry == nby:                                           # 만약 두 공이 겹쳤다면                             
                if rcnt > bcnt:                                                     # 이동거리가 많은 것을 뒤로 한 칸 이동시킨다.
                    nrx -= dx[i]                                                    
                    nry -= dy[i]
                else:
                    nbx -= dx[i]
                    nby -= dy[i]
            
            if not visited[nrx][nry][nbx][nby]:                                     # 탐색한 적이 없는 경우라면                
                queue.append((nrx, nry, nbx, nby, depth+1))                         # queue에 넣어주고 방문처리를 해준다.
                visited[nrx][nry][nbx][nby] = True                                  

if result == False: print(-1)