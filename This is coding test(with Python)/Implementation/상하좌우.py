# 맨 처음 내 풀이
n = int(input())
motions = input().split()

x = 1; y = 1
'''
U의 경우 행의 값을 -1해야 한다. 따라서 x 값만 1보다 크면 이동이 가능하다.
다른 이동 명령도 동일하게 처리해주면 아래와 같이 코드 작성이 가능하다.
가장 간단한 방식이고, 실행 시간도 가장 적을 것 같다.
'''
for i in motions:
    if i == 'U' and x > 1:
        x -= 1
    elif i == 'D' and x < n:
        x += 1
    elif i == 'R' and y < n:
        y += 1
    elif i == 'L' and y > 1:
        y -= 1

print(x, y)

'''
아래는 책의 코드이다.
'''

n = int(input())
x = 1; y = 1
plans = input().split()

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_type = ['L', 'R', 'U', 'D']

for plan in plans:
    for i in range(len(move_type)):
        # 이동 입력을 move_type 입력에서 확인해야 한다.
        if plan == move_type[i]:
            nx = x + dx[i]
            ny = y + dy[i]
    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue

    x, y = nx, ny

print(x, y)

# 2021.11.04 코드
n = int(input()) # 공간의 크기
movements = input().split() # 움직임

'''
책의 코드에서는 최악의 경우 4번을 반복해 이동 명령이 U, D, R, L인지 확인하고
위치를 이동시켰다.
딕셔너리를 통해 각 이동 좌표를 바로 찾을 수 있도록 개선했다.
맨 처음 고안한 방식이 가장 간편한 코드지만
책과 이 코드처럼 명령마다 이동 방식을 미리 저장하는 방식은 여러 알고리즘에서 응용이 가능하다.
잘 기억해두자.
'''

moving = {'U':(-1, 0), 'D':(1, 0), 'R':(0, 1), 'L':(0, -1)} # u, d, r, l

location = [1, 1]
for i in movements:
    after_row = location[0] + moving[i][0]
    after_col = location[1] + moving[i][1]

    if after_row < 1 or after_row > n or after_col < 1 or after_col > n:
        continue
    
    location[0] = after_row
    location[1] = after_col

print(location[0], location[1])