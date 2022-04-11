from copy import deepcopy
def solution(key, lock):
    n, m = len(lock), len(key)
    expanded_lock = [[0 for i in range(n+2*m)] for i in range(n+2*m)]
    
    for i in range(n):
        for j in range(n):
            expanded_lock[m+i][m+j] = lock[i][j]
    
    rotated_key = deepcopy(key)
    for r in range(4):
        rotated_key = list(zip(*rotated_key[::-1]))
        
        for x in range(1, n+m):
            for y in range(1, n+m):
                
                for i in range(m):
                    for j in range(m):
                        expanded_lock[x+i][y+j]+=rotated_key[i][j]
                
                if check(expanded_lock, n, m):
                    return True
                
                for i in range(m):
                    for j in range(m):
                        expanded_lock[x+i][y+j]-=rotated_key[i][j]
                        
    return False

def check(expanded_lock, n, m):
    lock = expanded_lock[m:m+n]
    
    for i in range(n):
        for j in range(n):
            if lock[i][m+j] != 1: return False
        
    return True
    
    
