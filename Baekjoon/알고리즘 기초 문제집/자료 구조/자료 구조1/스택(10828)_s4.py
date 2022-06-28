import sys
input = sys.stdin.readline

'''
push x: 정수 x를 스택에 넣는 연산
pop: 스택에서 가장 위에 있는 정수 제거 후 출력, 없으면 -1 출력
size: 들어있는 정수 개수 출력
empty: 스택이 비어있으면 1, 아니면 0출력
top: 스택의 가장 위에 있는 정수 출력, 없으면 -1출력
'''
 
stack = []          

for _ in range(int(input())):
    command = input().split()
    
    if command[0] == 'push':
        stack.append(command[1])
        
    elif command[0] == 'pop':
        if stack: print(stack.pop())
        else: print(-1) 
    
    elif command[0] == 'size':
        print(len(stack))
    
    elif command[0] == 'empty':
        if stack: print(0)
        else: print(1)
    
    elif command[0] == 'top':
        if stack: print(stack[-1])
        else: print(-1)
    