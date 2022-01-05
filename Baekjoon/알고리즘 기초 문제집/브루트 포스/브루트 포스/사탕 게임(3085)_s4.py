# 2021.11.07
import sys
input = sys.stdin.readline

n = int(input())

board = []
for _ in range(n):
    board.append(list(input().rstrip()))


'''
완전 탐색으로 풀어야겠다는 생각은 문제를 보자마자 들었지만, 
코드를 생각하는데 굉장히 힘들었다.
데이터 값을 바꿀 때 같은지 확인을 하고 같지않으면 바꾸고 같은면 바꿔야겠다는 생각이 오히려 독이된 것 같다.
계속 생각하다 보니 데이터가 같든 다르든 바꾸고 확인하면 된다는 것을 깨달았고 이를 코드로 작성했다.
앞으로 brute force문제 및 구현 문제는 많이 접해봐야 할 것 같다.
'''

def check_board(row, col):
    result = 0
    movements = [(1, 0), (-1, 0), (0, -1), (0, 1)]

    # 위 아래 데이터 값을 바꾼다.
    for i in movements[:4]:
        row_count = 1 # 위 아래 연속값
        col_count = 1 # 양 옆 연속값
        x = row + i[0]; y = col + i[1]
        if x < 0 or x >= n or y < 0 or y >= n: continue # 범위를 넘는지 확인한다.
        
        board[row][col], board[x][y] = board[x][y], board[row][col] # 두 값을 바꿔준다.
        # 위 아래를 확인한다.
        # row+1 ~ n-1까지 확인한다.
        for nx in range(row+1, n):
            if board[row][col] == board[nx][col]: row_count += 1
            else: break

        # 0 ~ row-1까지 확인한다.
        for nx in range(row-1, -1, -1):
            if board[row][col] == board[nx][col]: row_count += 1
            else: break
        
        # 양 옆을 동일한 방식으로 확인한다.
        for ny in range(col+1, n):
            if board[row][col] == board[row][ny]: col_count += 1
            else: break
        for ny in range(col-1, -1, -1):
            if board[row][col] == board[row][ny]: col_count += 1
            else: break

        board[row][col], board[x][y] = board[x][y], board[row][col] # 두 값을 바꿔준다.
        result = max(result, row_count, col_count)
    
    return result

result = 1
for x in range(n):
    for y in range(n):
        result = max(result, check_board(x, y))

print(result)