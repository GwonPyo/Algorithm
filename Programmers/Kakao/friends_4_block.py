def solution(n, m, board):
    board = [list(i) for i in board] # abcde 형태로 입력 받으므로 리스트 형태로 바꿔준다. 
    answer = 0                       # answer = 0 
    success_array = [1]              # success_array에는 아래에서 check 조건에 맞는 i, j를 튜플 형태로 넣어준다. (아래 반복문을 위해서 처음에는 [1]로 선언한다.)
    while success_array:             # 만약 success_array에 만족하는 i, j값이 없었다면 더 이상 탐색할 필요가 없으므로 반복문을 종료한다.
        success_array = []           # 빈 리스트로 초기화 해준다.
        for i in range(n): 
            for j in range(m):
                if check(board, i, j, n, m):
                    success_array.append((i, j))
        
        for x, y in success_array:   # success_array에 있는 값들을 0으로 바꿔준다.
            delete(board, x, y)
        rebuild(board, n, m)         # 0으로 바꾼 값들은 위로 올려 board를 rebuilding한다.
        answer += count(board, n, m) # 값이 0인 원소들은 모두 -1로 바꾼다. 
    
    return answer

def check(board, start_row, start_col, max_row, max_col):
    if max_row-start_row <= 1 or max_col-start_col <= 1: return False # 인덱스 범위를 만족하지 않으면 False를 반환한다.
    
    value = board[start_row][start_col]                                
    if value == -1: return False                                      # -1은 위 코드에서 아무 의미 없는 값이므로 값이 -1이라면 False를 반환한다.
    dx = [1, 1, 0]              
    dy = [0, 1, 1]
    
    for i in range(3):                                                # 2×2 배열의 값이 모두 같아야 하므로 주위의 모든 원소와 비교해본다.
        if value != board[start_row+dx[i]][start_col+dy[i]]:          # 만약 값이 다르다면 False를 반환한다.
            return False                            
    return True                                                       # 모두 같은 값을 가진다면 탐색을 시작한 row, col을 저장하도록 True를 반환한다.

def delete(board, x, y):                                              # 입력받은 i, j(x, y)와 주위 3개의 원소를 0으로 바꿔주는 함수다.
    board[x][y] = 0
    board[x+1][y] = 0
    board[x][y+1] = 0
    board[x+1][y+1] = 0
    
def rebuild(board, max_row, max_col):                                 # 값이 0인 원소들을 위로 올려주는 함수다.
    for i in range(1, max_row):
        for j in range(0, max_col):
            if board[i][j] == 0:
                for x in range(i, 0, -1):                             # 만약 값이 0인 원소를 찾았다면
                    board[x][j] = board[x-1][j]                       # 위에 있는 값을 저장하고
                    board[x-1][j] = 0                                 # 0을 위로 올려준다.
                    
def count(board, max_row, max_col):                                   # 0으로 바뀐 값을 세어주고 이후 다시 세지 않도록 -1로 바꿔주는 함수다.
    result = 0
    for i in range(max_row):
        for j in range(max_col):
            if board[i][j] == 0:                                      # 만약 값이 0이라면
                result += 1                                           # result에 1을 더하고 -1로 값을 변경한다.
                board[i][j] = -1
    return result
