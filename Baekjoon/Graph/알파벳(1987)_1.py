import sys
input = sys.stdin.readline

def dfs(x, y, tmp):
    global result
    result = max(result, tmp)
    index = ord(board[x][y])-ord("A")
    visited[index] = True
    
    for i in range(4):
        next_x, next_y = x+dx[i], y+dy[i]
        if next_x < 0 or next_x >= row or next_y < 0 or next_y >= col:
            continue
        
        next_index = ord(board[next_x][next_y])-ord("A")
        if not visited[next_index]:
            dfs(next_x, next_y, tmp+1)
                
    visited[index] = False
    
row, col = map(int, input().split()) # row, col: board판의 row, col을 의미
board = [] # board: board판의 정보를 담은 리스트
visited = [False for _ in range(26)] # visited: 방문한 알파벳을 체크하는 리스트
result = 0

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

for _ in range(row):
    board.append(tuple(input().rstrip()))    

dfs(0, 0, 1)

print(result)