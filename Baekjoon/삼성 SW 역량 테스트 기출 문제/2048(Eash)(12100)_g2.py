import sys
input = sys.stdin.readline

def top(n, depth, board):
    new_board = [[0 for _ in range(n)] for _ in range(n)]
    rows_index = [0 for _ in range(n)]
    
    for r_index in range(n):  
        for c_index, value in enumerate(board[r_index]):
            if value == 0: continue
            new_board[rows_index[c_index]][c_index] = value
            rows_index[c_index] += 1
    for c_index in range(n):
        for r_index in range(n-1):
            if new_board[r_index][c_index] != new_board[r_index+1][c_index]: continue
            if new_board[r_index][c_index] == 0: break
            
            new_board[r_index][c_index] += new_board[r_index+1][c_index]
            new_board[r_index+1][c_index] = 0
            for i in range(r_index+1, n-1):
                if new_board[i+1][c_index] == 0: break
                new_board[i][c_index] = new_board[i+1][c_index]
                new_board[i+1][c_index] = 0
    
    return depth+1, new_board

def bottom(n, depth, board):
    new_board = [[0 for _ in range(n)] for _ in range(n)]
    rows_index = [n-1 for _ in range(n)]
    
    for r_index in range(n-1, -1, -1):  
        for c_index, value in enumerate(board[r_index]):
            if value == 0: continue
            new_board[rows_index[c_index]][c_index] = value
            rows_index[c_index] -= 1
    
    for c_index in range(n):
        for r_index in range(n-1, 0, -1):
            if new_board[r_index][c_index] != new_board[r_index-1][c_index]: continue
            if new_board[r_index][c_index] == 0: break
            
            new_board[r_index][c_index] += new_board[r_index-1][c_index]
            new_board[r_index-1][c_index] = 0
            for i in range(r_index-1, 0, -1):
                if new_board[i-1][c_index] == 0: break
                new_board[i][c_index] = new_board[i-1][c_index]
                new_board[i-1][c_index] = 0
    
    return depth+1, new_board

def left(n, depth, board):
    new_board = [[0 for _ in range(n)] for _ in range(n)]
    cols_index = [0 for _ in range(n)]
    
    for r_index in range(n):  
        for value in board[r_index]:
            if value == 0: continue
            new_board[r_index][cols_index[r_index]] = value
            cols_index[r_index] += 1
    
    for r_index in range(n):
        for c_index in range(n-1):
            if new_board[r_index][c_index] != new_board[r_index][c_index+1]: continue
            if new_board[r_index][c_index] == 0: break
            
            new_board[r_index][c_index] += new_board[r_index][c_index+1]
            new_board[r_index][c_index+1] = 0
            for i in range(c_index+1, n-1):
                if new_board[r_index][i+1] == 0: break
                new_board[r_index][i] = new_board[r_index][i+1]
                new_board[r_index][i+1] = 0
    
    return depth+1, new_board

def right(n, depth, board):
    new_board = [[0 for _ in range(n)] for _ in range(n)]
    cols_index = [(n-1) for _ in range(n)]
    
    for r_index in range(n):  
        for value in board[r_index][::-1]:
            if value == 0: continue
            new_board[r_index][cols_index[r_index]] = value
            cols_index[r_index] -= 1
    
    for r_index in range(n):
        for c_index in range(n-1, 0, -1):
            if new_board[r_index][c_index] != new_board[r_index][c_index-1]: continue
            if new_board[r_index][c_index] == 0: break
            
            new_board[r_index][c_index] += new_board[r_index][c_index-1]
            new_board[r_index][c_index-1] = 0
            for i in range(c_index-1, 0, -1):
                if new_board[r_index][i-1] == 0: break
                new_board[r_index][i] = new_board[r_index][i-1]
                new_board[r_index][i-1] = 0
    
    return depth+1, new_board

n = int(input())                                                         # n: 보드 크기(n*n)
boards = [(0, [list(map(int, input().split())) for _ in range(n)])]      # board: 보드들을 모아 놓을 리스트

result = 0
while boards:
    depth, board = boards.pop(-1)
    
    result = max(result, max(map(max, board))) 
    
    if depth < 5:
        boards.append(top(n, depth, board))
        boards.append(bottom(n, depth, board))
        boards.append(left(n, depth, board))
        boards.append(right(n, depth, board))

print(result)
    