import sys
input = sys.stdin.readline

def bfs():
    global result
    
    queue = set([(0, 0, board[0][0])])
    
    while queue:
        x, y, visited_alphas = queue.pop()
        result = max(result, len(visited_alphas))
        
        for i in range(4):
            next_x, next_y = x+dx[i], y+dy[i]
            if next_x < 0 or next_x >= row or next_y < 0 or next_y >= col:
                continue
            
            next_alpha = board[next_x][next_y]
            if next_alpha not in visited_alphas:
                queue.add((next_x, next_y, visited_alphas+next_alpha))
                
row, col = map(int, input().split()) # row, col: board판의 row, col을 의미
board = [] # board: board판의 정보를 담은 리스트
result = 0

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

for _ in range(row):
    board.append(tuple(input().rstrip()))    

bfs()
print(result)