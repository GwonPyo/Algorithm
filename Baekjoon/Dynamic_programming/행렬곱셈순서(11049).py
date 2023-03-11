import sys
input = sys.stdin.readline

n = int(input())        # n: 행렬의 개수
matrix_list = list()    # matrix_list: 행렬의 크기를 담을 리스트
for _ in range(n):     
    matrix = tuple(map(int, input().split()))
    matrix_list.append(matrix)

dp = [[0 for i in range(n)] for i in range(n)] # N×N dp table 선언

for len_multi in range(1, n):
    # len_multi: 곱셈 길이 [Ex) A×B의 경우 len_multiply=1이다.]
    for start_matrix in range(0, n-len_multi):
        # start_matrix: 곱셈을 시작할 행렬의 번호를 의미한다. [Ex) 곱셈을 시작할 행렬이 A인 경우 start_matrix=0이다.]
        end_matrix = start_matrix + len_multi
        dp[start_matrix][end_matrix] = float("inf")
        
        for center_matrix in range(start_matrix, end_matrix):
            multi_row = matrix_list[start_matrix][0]
            multi_cen = matrix_list[center_matrix][1]
            multi_col = matrix_list[end_matrix][1]
            temp = dp[start_matrix][center_matrix]+dp[center_matrix+1][end_matrix]+multi_row*multi_cen*multi_col
            
            dp[start_matrix][end_matrix] = min(dp[start_matrix][end_matrix], temp)

print(dp[0][-1])