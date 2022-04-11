import sys
input = sys.stdin.readline

n = int(input())

result = 0
row = [0 for _ in range(n)]

def possible(x):
    for i in range(x):
        if row[x]==row[i] or abs(row[x]-row[i])==abs(x-i):
            return False
    return True

def dfs(x):
    global result
    if x == n:
        result += 1
        return

    for i in range(n):
        row[x] = i
        if possible(x):
            dfs(x+1)

dfs(0)
print(result)
