row, column = map(int, input().split())
char_x, char_y, direction = map(int, input().split())
    
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

Map = []
for _ in range(row):
    Map.append(list(map(int, input().split())))    

count = 0
stack = [(char_x, char_y, direction)]

while stack:
    x, y, direction = stack.pop()
    Map[x][y] = 1
    count += 1
    for _ in range(4):
        if Map[x + dx[direction]][y + dy[direction]] == 0: 
            stack.append((x + dx[direction], y + dy[direction], direction))
        direction += 1
        if direction > 3:
            direction = 0

print(count)